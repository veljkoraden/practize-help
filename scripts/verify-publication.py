#!/usr/bin/env python3
"""Verify deployed Help pages against the immutable publication manifest."""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ALLOWED_ORIGIN = "https://help.practize.io"


class PageMetadata(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonical = None
        self.corpus_id = None
        self.source_sha256 = None
        self.in_h1 = False
        self.h1 = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")
        if tag == "meta" and values.get("name") == "practize-corpus-id":
            self.corpus_id = values.get("content")
        if tag == "meta" and values.get("name") == "practize-source-sha256":
            self.source_sha256 = values.get("content")
        if tag == "h1":
            self.in_h1 = True

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1.append(data)


def validate_url(url: str) -> None:
    parsed = urlparse(url)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "help.practize.io"
        or parsed.username
        or parsed.password
        or parsed.port
        or parsed.query
        or parsed.fragment
        or not parsed.path.startswith("/help/")
    ):
        raise ValueError(f"unsafe canonical URL: {url}")


def fetch(url: str, opener=urlopen):
    request = Request(url, headers={"User-Agent": "PractizePublicationVerifier/1.0"})
    with opener(request, timeout=20, context=ssl.create_default_context()) as response:
        return response.getcode(), response.geturl(), response.read().decode("utf-8")


def verify_document(document: dict, opener=urlopen) -> None:
    url = document["url"]
    validate_url(url)
    status, final_url, body = fetch(url, opener)
    if status != 200:
        raise ValueError(f"{document['id']}: HTTP {status}")
    if final_url.rstrip("/") != url.rstrip("/"):
        raise ValueError(f"{document['id']}: redirected to {final_url}")

    metadata = PageMetadata()
    metadata.feed(body)
    if metadata.canonical != url:
        raise ValueError(f"{document['id']}: canonical mismatch")
    if metadata.corpus_id != document["id"]:
        raise ValueError(f"{document['id']}: corpus ID mismatch")
    if metadata.source_sha256 != document["sha256"]:
        raise ValueError(f"{document['id']}: source SHA-256 mismatch")
    if not "".join(metadata.h1).strip():
        raise ValueError(f"{document['id']}: missing H1")


def verify(manifest: dict, opener=urlopen) -> dict:
    documents = manifest.get("documents")
    if not isinstance(documents, list) or len(documents) != 25:
        raise ValueError("publication manifest must contain exactly 25 documents")
    ids = [document.get("id") for document in documents]
    urls = [document.get("url") for document in documents]
    if len(set(ids)) != len(ids) or len(set(urls)) != len(urls):
        raise ValueError("publication manifest contains duplicate IDs or URLs")
    for document in documents:
        verify_document(document, opener)
    return {
        "status": "verified",
        "origin": ALLOWED_ORIGIN,
        "manifest_version": manifest.get("source_manifest_version"),
        "documents": len(documents),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path("publication-manifest.json"))
    parser.add_argument("--attempts", type=int, default=4)
    parser.add_argument("--retry-delay", type=float, default=3)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    last_error = None
    for attempt in range(1, args.attempts + 1):
        try:
            print(json.dumps(verify(manifest), separators=(",", ":")))
            return 0
        except (OSError, ValueError, UnicodeError) as error:
            last_error = error
            if attempt < args.attempts:
                time.sleep(args.retry_delay)
    print(f"publication verification failed: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
