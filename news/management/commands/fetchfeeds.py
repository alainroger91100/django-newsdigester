from django.core.management.base import BaseCommand
from news.tasks import fetch_feeds


class Command(BaseCommand):
    help = 'Run the fetch_feeds task synchronously (useful for manual runs)'

    def handle(self, *args, **options):
        # run synchronously so it works without Celery installed
        result = fetch_feeds()
        self.stdout.write(self.style.SUCCESS(f"fetch_feeds finished: {result}"))