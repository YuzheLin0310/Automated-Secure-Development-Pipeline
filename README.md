# Person A - App + Security

This package contains the **Person A** portion of the Automated Secure Development Pipeline project described in the uploaded document. It includes:

- `app/app_insecure.py` - intentionally vulnerable Flask demo app
- `app/app_fixed.py` - remediated version of the same app
- `app/requirements_insecure.txt` - intentionally outdated dependency example
- `app/requirements_fixed.txt` - updated dependency example

## Intentional vulnerabilities in the insecure version

- Hardcoded API key
- MD5 password hashing
- Unsafe subprocess call with `shell=True`
- Flask debug mode enabled
- Outdated Flask dependency

## Fixes in the secure version

- API key moved to environment variable
- MD5 replaced with SHA-256
- `shell=True` removed
- Debug mode disabled
- Dependency updated

## Run locally

### Insecure version

```bash
cd app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_insecure.txt
python app_insecure.py
```

### Fixed version

```bash
cd app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_fixed.txt
export DEMO_API_KEY="your-demo-key"
python app_fixed.py
```

## Suggested local security scans

```bash
bandit -r .
semgrep --config=auto .
pip-audit -r requirements_insecure.txt
```
