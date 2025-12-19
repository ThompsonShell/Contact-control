#!/bin/sh
set -e

: "${DB_HOST:=db}"
: "${DB_PORT:=5432}"
: "${POSTGRES_USER:=django}"

echo "Waiting for Postgres at ${DB_HOST}:${DB_PORT}..."

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$POSTGRES_USER" >/dev/null 2>&1; do
  echo "Postgres not ready - sleeping"
  sleep 1
done

echo "Postgres is available — running migrations and collectstatic"

python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

    
exec "$@"
