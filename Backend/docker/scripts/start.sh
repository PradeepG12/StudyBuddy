#!/bin/sh

until nc -z redis 6379; do
    echo "Redis is DOWN!"
    sleep 1
done
echo "Redis is UP!"

python manage.py runserver 0.0.0.0:8000 &
daphne -b 0.0.0.0 -p 8081 base.asgi:application