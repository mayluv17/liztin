#!/bin/sh

if [ "$DATABASE" = "postgress"] 
then
    echo "checking if database is running"

    while ! nc -z $SQL_HOST $SQL_PPPORT; do
        sleep 0.1
    done

    echo "The database is up and running :-D"
fi

python manage.py makemigrations
python manage.py migrate
exec "$@"

