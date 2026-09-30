# roytsmart.github.io

Source for my personal website, <https://roytsmart.github.io>, built with
Sphinx and the PyData Sphinx Theme.

## Building locally

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt sphinx-autobuild   # .venv/bin on Linux/macOS
.venv/Scripts/sphinx-autobuild . _build/html                     # live preview at http://127.0.0.1:8000
```

Pushing to `main` builds the site with `sphinx-build -W` and deploys it to
GitHub Pages; pull requests only run the build.
