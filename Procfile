web: gunicorn manage:app --reload
worker: celery worker -A app.worker.celery --loglevel=INFO