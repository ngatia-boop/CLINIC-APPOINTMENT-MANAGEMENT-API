# Clinic Appointment - Project Layout

This repository uses a Flask backend and a React + TypeScript frontend. The README below describes the recommended project structure, conventions and common commands to develop, test and deploy.

## Top-level layout
- backend/        - Flask application (Python)
- frontend/       - React + TypeScript (Vite)
- infra/          - Docker, Kubernetes, or cloud infra manifests
- docs/           - Architecture docs, API contracts, ER diagrams
- scripts/        - Helper scripts (seed, migrations helpers, CI helpers)
- tests/          - Integration / e2e tests (if not colocated)
- .env.example    - Example environment variables
- docker-compose.yml

---

## Backend (backend/)
Suggested structure (factory pattern, modular blueprints):
- backend/
  - app/
    - __init__.py         # create_app factory, blueprint registration
    - config.py           # env-specific config classes
    - extensions.py       # db, migrate, jwt, cors, ma, etc.
    - models/             # SQLAlchemy models
    - schemas/            # Marshmallow / Pydantic schemas
    - api/
      - v1/
        - auth/
        - appointments/
        - users/
    - services/           # business logic, use-case layer
    - repositories/       # db access abstraction
    - utils/              # helpers, validators
    - cli.py              # custom flask CLI commands
    - tests/              # backend unit tests
  - migrations/           # Alembic / Flask-Migrate files
  - requirements.txt
  - Dockerfile
  - wsgi.py / run.py

Best practices:
- Use application factory and configuration objects.
- Keep request parsing in schemas and business logic in services.
- Use Flask-Migrate for DB schema changes.
- Centralize extensions in extensions.py to avoid circular imports.

Common commands:
- python -m venv .venv && source .venv/bin/activate
- pip install -r backend/requirements.txt
- export FLASK_APP=backend.app:create_app
- flask db upgrade
- flask run

---

## Frontend (frontend/)
Typical Vite + React + TypeScript layout:
- frontend/
  - package.json
  - tsconfig.json
  - vite.config.ts
  - public/               # static assets, index.html
  - src/
    - main.tsx            # app bootstrap
    - App.tsx
    - api/                # api client (axios / fetch wrappers)
    - services/           # calls coordinating multiple api endpoints
    - hooks/              # reusable hooks (useAuth, useFetch)
    - features/           # domain folders (appointments, users)
      - appointments/
        - components/
        - pages/
        - types.ts
        - hooks.ts
    - components/         # shared UI components
    - pages/              # top-level pages / routes
    - routes/             # react-router setup
    - contexts/           # React contexts
    - store/              # global state (RTK / Zustand / Context)
    - types/              # shared TypeScript types
    - styles/             # global styles, theme
    - tests/              # frontend tests (Jest / Testing Library)
  - Dockerfile

Best practices:
- Keep domain logic in feature folders.
- Type API responses and form data.
- Provide an API client that centralizes base URL, auth headers, and error handling.
- Use env files (.env.development/.env.production) for API base URLs and feature flags.

Common commands:
- cd frontend
- npm install
- npm run dev
- npm run build
- npm run test
- npm run lint / npm run format

---

## Development workflow
- Run backend and frontend concurrently (use docker-compose or tools like concurrently)
- Configure CORS on the backend and a proxy in frontend dev if needed
- Use .env.example for required environment variables and do not commit secrets
- Run linters and formatters pre-commit (Black, isort, flake8 for Python; Prettier, ESLint, TypeScript for frontend)
- Write unit tests for services and components; write integration tests for endpoints and flows

Example dev run (local):
- backend: FLASK_ENV=development FLASK_APP=backend.app:create_app flask run
- frontend: cd frontend && npm run dev

---

## Deployment
Options:
- Build frontend into static files and serve via Nginx (or CDN), backend as Gunicorn + workers behind a reverse proxy.
- Use Docker images and deploy with docker-compose, ECS, GKE, or other providers.
- Secure secrets with a secret manager; use environment-specific config classes.

Production tips:
- Enable strict CORS and auth.
- Use HTTPS and set secure cookies.
- Run database migrations during deploy pipeline.

---

## Testing & CI
- Backend: pytest, fixtures, factory boy for test objects; run migrations in CI test job.
- Frontend: Jest + React Testing Library; include basic accessibility checks.
- CI pipeline should run: lint -> test -> build -> (optionally) deploy
- Include test coverage thresholds and fail on regressions.

---

## Conventions & Notes
- Use feature/ or hotfix/ branches and follow PR reviews.
- Keep controllers thin; put logic in services.
- Centralize error handling and API response formats.
- Maintain an up-to-date README in both backend/ and frontend/ with their own developer setup steps.

---

For quick onboarding, add docs/DEVELOPER.md with step-by-step setup for new contributors (virtualenv setup, node version, env variables, running both apps).
