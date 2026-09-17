"""Dependency-free checks for the public results-page export."""
from pathlib import Path
from html.parser import HTMLParser

root = Path(__file__).parent / 'site'
class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value and not value.startswith('#'):
                assert '://' not in value, f'Unexpected external resource: {value}'
                assert (root / value.split('?')[0]).is_file(), f'Missing asset: {value}'

html = (root / 'index.html').read_text()
Links().feed(html)
assert html.count('<figure ') == 9
for value in ('docs.google.com', 'drive.google.com', '/Users/', 'reports_index.csv', 'api_key', 'PRIVATE KEY'):
    assert value not in html, f'Unexpected private reference: {value}'
allowed = {'.html', '.css', '.png', '.pdf', '.svg', '.json'}
assert all(p.suffix in allowed for p in root.rglob('*') if p.is_file())
assert not list(root.rglob('*.prompt.*')), 'Generation prompts must not be published'
assert (root / 'assets/illustrative-inheritance-dag-v2.pdf').is_file()
print('PASS: nine figures, all local links resolve, no prompts or prohibited private references.')
