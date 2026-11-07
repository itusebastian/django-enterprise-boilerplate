# Django Enterprise Boilerplate

[![CI](https://github.com/itusebastian/django-enterprise-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/itusebastian/django-enterprise-boilerplate/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Django 6.1](https://img.shields.io/badge/django-6.1-green.svg)](https://www.djangoproject.com/)
[![Ruff](https://img.shields.io/badge/code%20style-Ruff-261230.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Django starter project with a UUID-based custom user model, email and social authentication, PostgreSQL support, and a Docker-based local development workflow. It also includes a small template-driven UI, pytest tests, and GitHub Actions checks.

## Features

| Area | Included |
| --- | --- |
| Authentication | Custom user model, email/password login, Google and GitHub sign-in via django-allauth |
| User data | UUID primary key, unique email, optional bio and avatar |
| Database | PostgreSQL via `DATABASE_URL` or `POSTGRES_URL`; SQLite fallback for local use |
| Templates | Django templates styled with Tailwind CSS from its CDN |
| Quality checks | Ruff and pytest with pytest-django |
| CI | GitHub Actions runs Ruff and tests against PostgreSQL 15 |
| Local containers | Dockerfile and Docker Compose development service |

## Architecture

```text
.
├── .github/workflows/ci.yml  # Lint and test workflow
├── config/                   # Django settings and URL routing
├── templates/                # Base, home, and django-allauth templates
├── users/                    # Custom user model, migration, and tests
├── static/css/               # Static CSS directory
├── pyproject.toml            # Project dependencies, pytest, and Ruff config
├── requirements.txt          # Pinned install requirements
├── Dockerfile                # Local development image
└── docker-compose.yml        # Local web service
```

The home page is served by `config/urls.py`. Authentication routes are provided by django-allauth under `/accounts/`. The `users` app defines the project user model, which is configured as `AUTH_USER_MODEL`.

## Requirements

- Python 3.12 or newer
- pip
- Docker Compose (optional)
- A PostgreSQL connection URL only when using PostgreSQL; SQLite is the default fallback

## Local setup

Clone the repository and create a virtual environment:

```sh
git clone https://github.com/itusebastian/django-enterprise-boilerplate.git
cd django-enterprise-boilerplate
python3.12 -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with `.venv\Scripts\activate`.

Install dependencies and create your local environment file:

```sh
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` before running the project. Set a private `SECRET_KEY`. For SQLite development, remove the sample `DATABASE_URL` line or replace it with a valid SQLite URL such as `sqlite:///db.sqlite3`. To use PostgreSQL, set `DATABASE_URL` to your PostgreSQL connection string; Neon connection strings are supported. `DATABASE_URL` takes precedence over `POSTGRES_URL`.

Google and GitHub credentials are required only to use those OAuth providers. Register OAuth applications with callback URLs:

- Google: `http://127.0.0.1:8000/accounts/google/login/callback/`
- GitHub: `http://127.0.0.1:8000/accounts/github/login/callback/`

Apply migrations and start Django:

```sh
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>.

## Docker development

Create and configure `.env` as described above, then build and start the web service:

```sh
docker compose up --build
```

In another terminal, apply migrations in the running container:

```sh
docker compose exec web python manage.py migrate
```

The app is available at <http://127.0.0.1:8000/>. The Docker image runs Django's development server and is intended for local development, not production deployment.

## Tests and lint

Run the test suite with SQLite and check lint locally:

```sh
DATABASE_URL="sqlite:///:memory:" pytest
ruff check .
```

GitHub Actions runs these checks on pushes and pull requests targeting `main`; the CI test job uses a PostgreSQL 15 service.

## Production considerations

This repository is a development starter, not a fully hardened production deployment. Before deploying, configure a production WSGI or ASGI server, secure `SECRET_KEY` and `DEBUG`, production `ALLOWED_HOSTS`, HTTPS and cookie settings, and production static-file handling. Configure provider credentials and the database through the deployment platform's secret management rather than committing them.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).