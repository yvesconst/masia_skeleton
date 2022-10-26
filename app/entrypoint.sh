echo "Waiting for postgres start ..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

python manage.py migrate

# static files
python manage.py collectstatic --no-input

exec "$@"
