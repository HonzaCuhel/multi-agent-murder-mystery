# Crosscurrents results page

[View the live results page](https://honzacuhel.github.io/multi-agent-murder-mystery/)

Minimal, dependency-free static research-results page. Only `site/` is intended for publication. No input data, scenario text, private document links, or trajectories are included.

## Preview

```sh
python3 -m http.server 4173 --directory site --bind 127.0.0.1
```

Open http://127.0.0.1:4173. The page uses relative URLs and works under a GitHub Pages repository subpath.

## GitHub Pages

The included deployment workflow runs manually, not on push. Configure the repository's Pages source as GitHub Actions, then run the Publish results page workflow when ready. It publishes only `site/`.

## Figures

The methodology flowchart and Figure A are displayed on the page with PDF downloads. Figure A is a separate illustrative story; it does not reveal the experimental scenario. Generation prompts are excluded from version control and deployment.

Figures B–I retain the article's lettering. Existing aggregate PNG figures and available PDFs are copied unchanged. Click each figure for the full-resolution PNG; PDF links are provided where a source PDF is available. No PDF was fabricated for Figure D.

## Evidence and caveats

Ten runs of one scenario, five monitor repetitions per configuration per run. Automated grading remains provisional. Standard deviations are not confidence intervals. No unresolved item receives correct credit. Percentages retain one decimal place; dollar totals retain two.
