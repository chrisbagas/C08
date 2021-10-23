migrate: bash deployment.sh
release: python manage.py migrate
web: gunicorn C08.wsgi --log-file -
