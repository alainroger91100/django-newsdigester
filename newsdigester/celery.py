import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsdigester.settings')

app = Celery('newsdigester')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# optional: default beat schedule example
from celery.schedules import crontab


app.conf.beat_schedule = {
    'fetch-feeds-every-2-minute': {
    'task': 'news.tasks.fetch_feeds',
    # run every 2 minutes (adjust as needed)
    'schedule': crontab(minute='*/2'),
    },
}
