#!/bin/bash

# Wait for the database to be ready
echo "Waiting for database..."
# while ! nc -z $DB_HOST $DB_PORT; do
#   sleep 0.1
# done
# echo "Database is ready!"


python manage.py collectstatic --noinput


python manage.py migrate

# Seed the database
python manage.py shell <<EOF
from dashboard.seed import seed
seed()
EOF

# Start the server
exec "$@"