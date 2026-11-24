"""Check rendered navigation, including every published article."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class Breadcrumbs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.labels = []
        self.links = []
        self.current = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'nav' and attrs.get('aria-label') == 'Breadcrumb':
            self.inside = True
        if not self.inside:
            return
        if tag == 'li':
            self.labels.append('')
        if tag == 'a':
            self.links.append(attrs.get('href'))
        if attrs.get('aria-current') == 'page':
            self.current += 1

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.inside = False

    def handle_data(self, data):
        if self.inside and self.labels and data.strip() != '/':
            self.labels[-1] += data


root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
manifest = json.loads(Path('publication-manifest.json').read_text())
cases = [('/', 'Product help'), ('/help/', 'Help articles'), ('/404.html', 'Page not found')]
cases += [(urlparse(doc['url']).path, doc['title']) for doc in manifest['documents']]
for url, title in cases:
    path = root / url.lstrip('/')
    candidates = [path, path / 'index.html', Path(str(path) + '.html')]
    path = next((candidate for candidate in candidates if candidate.is_file()), None)
    assert path is not None, f'Missing rendered page: {url}'
    parser = Breadcrumbs()
    parser.feed(path.read_text())
    expected = [] if url == '/' else ['Home']
    links = [] if url == '/' else ['/']
    if url not in ('/', '/help/'):
        expected.append('Help articles')
        links.append('/help/')
    if url.startswith('/help/apps/'):
        expected.append('Apps')
        links.append('/help/apps')
    if url != '/':
        expected.append(title)
    assert [label.strip() for label in parser.labels] == expected, url
    assert parser.links == links, url
    assert parser.current == (0 if url == '/' else 1), url
print(f'Breadcrumb checks passed for {len(cases)} rendered pages.')
