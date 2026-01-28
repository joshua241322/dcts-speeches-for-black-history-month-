release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn bhm_site.wsgi --bind 0.0.0.0:8000