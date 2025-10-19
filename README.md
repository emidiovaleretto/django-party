# django-party

[![Django CI](https://github.com/emidiovaleretto/django-party/actions/workflows/django.yml/badge.svg)](https://github.com/emidiovaleretto/django-party/actions/workflows/django.yml)

Simple party management app built with Django 5 and Tailwind CSS, featuring HTMX and Alpine.js for interactivity.

---

## 🔎 Quick health check

Run these to verify your environment and project wiring:

```bash
# 1) Python env and deps
python -V
python -m pip --version
python -m pip install -r requirements.txt

# 2) Node deps and Tailwind build
node --version
npm --version
npm install
npm run tailwind:build

# 3) Django system checks and DB
python manage.py check
python manage.py migrate

# 4) Lint (PEP8) and tests
./scripts/check_formatting.sh
pytest -q
```

If any step fails, see Troubleshooting below.

---

## ✨ Features

- Django 5.1 with a custom user model (`party.CustomUser`)
- Tailwind CSS with custom theme and components
- HTMX and Alpine.js loaded from Django static files
- Party list view for the logged-in host, showing parties from today forward
- Pytest test suite and CI workflow

---

## 🧰 Requirements

- Python 3.10–3.12 (matches CI matrix)
- Node.js 18+ (recommended) and npm
- SQLite (default)

---

## ⚙️ Setup

1) Clone and create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# On Windows: .venv\\Scripts\\activate
```

2) Install Python deps

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3) Install Node deps and build Tailwind once

```bash
npm install
npm run tailwind:build
```

4) Configure environment

Create a `.env` file in the project root (Django reads it via python-decouple):

```env
SECRET_KEY=django-insecure-local-dev-key
DEBUG=True
```

5) Migrate and load optional fixtures

```bash
python manage.py migrate
# Optional demo data (adjust as needed):
python manage.py loaddata party/fixtures/initial_guests.json
python manage.py loaddata party/fixtures/initial_gifts.json
python manage.py loaddata party/fixtures/initial_parties.json
```

6) Create a superuser (optional)

```bash
python manage.py createsuperuser
```

---

## 🧪 Run and develop

- Start Tailwind in watch mode (rebuilds on change):

```bash
npm run tailwind:dev
```

- Run the Django dev server:

```bash
python manage.py runserver
```

- Visit the app: http://127.0.0.1:8000/

Note: The party list view requires authentication (`LoginRequiredMixin`). Log in via the admin or your own login flow. If you prefer Django’s built-in auth views, add the following route to `core/urls.py`:

```python
# core/urls.py
path('accounts/', include('django.contrib.auth.urls')),
```

---

## ✅ Linting and formatting

- Check PEP8 compliance:

```bash
./scripts/check_formatting.sh
```

- Auto-fix common issues (unused imports, spacing, etc.):

```bash
./scripts/fix_formatting.sh
```

Configuration is in `.flake8`. CI runs the checks automatically.

---

## 🧪 Tests

Run the test suite with pytest:

```bash
pytest -q
```

Pytest is configured via `pytest.ini` with `DJANGO_SETTINGS_MODULE=core.settings`.

---

## 🎨 Tailwind CSS

- Config: `tailwind.config.js` (scans app templates and root `templates/`)
- Input CSS: `party/static/party/src/main.css`
- Output CSS: `party/static/party/css/tailwind_output.css`

Important:
- Put your custom CSS in the input file, not in the output (the output is overwritten).
- Keep the order in `main.css`:
  - `@tailwind base;`
  - `@tailwind components;`
  - custom components inside `@layer components { ... }`
  - `@tailwind utilities;`
- Root templates are scanned, so classes used in `templates/base.html` are preserved.

---

## 📁 Project structure

```
django-party/
├─ core/
│  ├─ settings.py
│  ├─ urls.py
├─ party/
│  ├─ models.py
│  ├─ urls.py
│  ├─ views/
│  │  └─ party_list_view.py
│  ├─ templates/party/party_list/
│  │  └─ page_parties_list.html
│  ├─ static/party/
│  │  ├─ js/ (htmx.min.js, alpine.min.js)
│  │  ├─ src/main.css (Tailwind input)
│  │  └─ css/tailwind_output.css (Tailwind output)
│  └─ fixtures/
├─ templates/
│  └─ base.html
├─ scripts/
│  ├─ check_formatting.sh
│  └─ fix_formatting.sh
├─ .github/workflows/django.yml
├─ requirements.txt
├─ package.json
```

---

## 🩺 Troubleshooting

- CSS changes don’t stick / custom classes missing
  - Ensure you’re editing `party/static/party/src/main.css` (not the output file).
  - Confirm Tailwind scans all relevant templates: `tailwind.config.js` should include `./party/templates/party/**/*.html` and `./templates/**/*.html`.
  - If classes are built dynamically, consider a `safelist` in Tailwind config.
  - Verify static paths in `templates/base.html` don’t have a leading `./` (use `{% static 'party/css/tailwind_output.css' %}`).

- Party list doesn’t render
  - The list view requires login. Log in first, or wire up auth routes via `django.contrib.auth.urls` as shown above.
  - Ensure the logged-in user has parties with `party_date >= today`.

- CI fails on flake8 not found
  - The workflow installs deps with `python -m pip install -r requirements.txt` and runs checks via `python -m flake8`.
  - See the “Show Python and flake8 info” step in CI logs for details.

---

## 📜 License

ISC

---

## 🙌 Credits

- Tailwind CSS
- HTMX
- Alpine.js
- Django