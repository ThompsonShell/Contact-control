# Contact-control

Dockerized Django + PostgreSQL project. PostgreSQL runs in its own container and is used internally by the web container. No external DB or mandatory host .env is required if credentials are provided in `docker-compose.yml`.

## Quick Start
1. Clone:
```bash
git clone https://github.com/ThompsonShell/Contact-control.git
cd Contact-control
```
2. Build & run:
```bash
docker compose up -d --build
```
3. View logs:
```bash
docker compose logs -f web
docker compose logs -f db
```

## DB init & check
- SQL files in `db/init/` are executed by the official Postgres image only on first initialization (when the DB volume is empty).
- Check seed data:
```bash
docker compose exec db psql -U <POSTGRES_USER> -d <POSTGRES_DB> -c "SELECT * FROM app.sample;"
```
- To force init scripts to run again (WARNING: deletes DB data):
```bash
docker compose down -v
docker compose up -d --build
```

## Useful commands
- Run migrations:
```bash
docker compose exec web python manage.py migrate --noinput
```
- Collect static files:
```bash
docker compose exec web python manage.py collectstatic --noinput
```
- Enter web container:
```bash
docker compose exec web bash
```

## Troubleshooting (short)
- Init SQL not applied → existing DB volume: `docker-compose down -v` then bring up again.
- Web errors before DB ready → ensure entrypoint waits for DB (e.g. `pg_isready`).

## AI assistance (what was done with AI)
1. Endpoint testing — suggested test commands and DB checks.  
2. README writing — this README was drafted with AI help.  
3. Docker guidance — Dockerfile, docker-compose, entrypoint and init-file usage were advised by AI.

