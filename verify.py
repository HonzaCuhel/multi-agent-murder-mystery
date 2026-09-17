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
assert html.count('<figure ') == 11
assert 'class="study"' not in html
assert 'class="brand"' not in html
assert 'src="assets/illustrative-inheritance-dag-v6.png"' in html
assert 'src="assets/methodology-flowchart-v3.png"' in html
for heading in ('How well were models able to reconstruct what happened?',
                'How much did models have to reason?',
                'How effective were models at reconstruction?'):
    assert heading in html
vectors = list(root.glob('assets/*.svg'))
assert len(vectors) == 8
for vector in vectors:
    svg = vector.read_text()
    assert '<image' not in svg and '<script' not in svg, vector.name
    assert '/Users/' not in svg and 'reports_index.csv' not in svg, vector.name
    assert f'src="assets/{vector.name}"' in html, vector.name
for value in ('docs.google.com', 'drive.google.com', '/Users/', 'reports_index.csv', 'api_key', 'PRIVATE KEY'):
    assert value not in html, f'Unexpected private reference: {value}'
allowed = {'.html', '.css', '.png', '.pdf', '.svg', '.json'}
assert all(p.suffix in allowed for p in root.rglob('*') if p.is_file())
assert not list(root.rglob('*.prompt.*')), 'Generation prompts must not be published'
assert (root / 'assets/illustrative-inheritance-dag-v6.pdf').is_file()
print('PASS: eleven figures, three results sections, all links resolve, no prompts or prohibited private references.')
