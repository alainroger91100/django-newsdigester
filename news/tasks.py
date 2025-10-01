import feedparser
from celery import shared_task
from django.utils import timezone
from dateutil import parser as dateparser
from .models import NewsSource, Article


@shared_task(name='news.tasks.fetch_feeds')
def fetch_feeds():
    """
    Fetch feeds from active sources and save new articles.
    
    This task avoids duplicates by using Article.link unique key and `get_or_create`.
    """
    created = 0
    for source in NewsSource.objects.filter(active=True):
        # print(source)
        parsed = feedparser.parse(source.rss_url)
        
        for entry in parsed.entries:
            link = entry.get('link') or entry.get('id')
            if not link:
                continue
            title = entry.get('title', 'No title')
            summary = entry.get('summary', '')

            # published handling: try multiple fields then fallback to now
            published = None
            for key in ('published', 'updated', 'pubDate'):
                val = entry.get(key)
                if val:
                    try:
                        published_dt = dateparser.parse(val)
                        if timezone.is_naive(published_dt):
                            published_dt = timezone.make_aware(published_dt, timezone.get_current_timezone())
                            published = published_dt
                            break
                    except Exception:
                        published = None

            if not published:
                # some feeds provide `published_parsed` (struct_time)
                if getattr(entry, 'published_parsed', None):
                    try:
                        published = timezone.make_aware(timezone.datetime(*entry.published_parsed[:6]))
                    except Exception:
                        published = None

            defaults = {
                'source': source,
                'title': title,
                'summary': summary,
                'published': published,
            }
            
            # Using get_or_create on link field to ensure Article.link is unique
            article, created_flag = Article.objects.get_or_create(link=link, defaults=defaults)
            if created_flag:
                created += 1
    return {'created': created}