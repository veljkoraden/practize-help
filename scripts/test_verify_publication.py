#!/usr/bin/env python3

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("verify-publication.py")
SPEC = importlib.util.spec_from_file_location("verify_publication", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Response:
    def __init__(self, url, body, status=200):
        self.url = url
        self.body = body.encode()
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None

    def getcode(self):
        return self.status

    def geturl(self):
        return self.url

    def read(self):
        return self.body


def document(number=0):
    return {
        "id": f"en.article-{number}",
        "url": f"https://help.practize.io/help/article-{number}",
        "sha256": f"{number:064x}",
    }


def html_for(item, canonical=None, corpus_id=None, sha256=None):
    return (
        '<html><head><link rel="canonical" href="%s">'
        '<meta name="practize-corpus-id" content="%s">'
        '<meta name="practize-source-sha256" content="%s"></head>'
        '<body><h1>Article</h1></body></html>'
    ) % (canonical or item["url"], corpus_id or item["id"], sha256 or item["sha256"])


class VerifyPublicationTest(unittest.TestCase):
    def test_verifies_exact_production_metadata(self):
        item = document()
        opener = lambda request, **_: Response(request.full_url, html_for(item))
        MODULE.verify_document(item, opener)

    def test_rejects_old_apex_host(self):
        item = document()
        item["url"] = "https://practize.io/help/article-0"
        with self.assertRaisesRegex(ValueError, "unsafe canonical"):
            MODULE.verify_document(item)

    def test_rejects_redirect(self):
        item = document()
        opener = lambda request, **_: Response("https://help.practize.io/help/other", html_for(item))
        with self.assertRaisesRegex(ValueError, "redirected"):
            MODULE.verify_document(item, opener)

    def test_rejects_canonical_id_hash_and_heading_mismatches(self):
        item = document()
        cases = [
            html_for(item, canonical=item["url"] + "/wrong"),
            html_for(item, corpus_id="en.other"),
            html_for(item, sha256="f" * 64),
            html_for(item).replace("<h1>Article</h1>", ""),
        ]
        for body in cases:
            opener = lambda request, body=body, **_: Response(request.full_url, body)
            with self.assertRaises(ValueError):
                MODULE.verify_document(item, opener)

    def test_requires_complete_unique_inventory(self):
        items = [document(number) for number in range(25)]
        opener = lambda request, **_: Response(
            request.full_url,
            html_for(next(item for item in items if item["url"] == request.full_url)),
        )
        report = MODULE.verify({"source_manifest_version": "v1", "documents": items}, opener)
        self.assertEqual(25, report["documents"])
        with self.assertRaisesRegex(ValueError, "exactly 25"):
            MODULE.verify({"documents": items[:-1]}, opener)
        items[-1] = dict(items[0])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            MODULE.verify({"documents": items}, opener)


if __name__ == "__main__":
    unittest.main()
