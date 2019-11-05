#!/bin/bash
set -e
cmd="$@"

function pg_ready(){
python << END
import sys
import psycopg2 as pg2
try:
    conn = pg2.connect("host=$DJANGO_DB_HOST dbname=$DJANGO_DB_NAME user=$DJANGO_DB_USERNAME password=$DJANGO_DB_PASSWORD port=$DJANGO_DB_PORT")
except:
    sys.exit(-1)
sys.exit(0)
END
}

until pg_ready; do
  >&2 echo "pg is unavailable - sleeping"
  sleep 1
done

>&2 echo "pg is up - continuing..."
exec $cmd