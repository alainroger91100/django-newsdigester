from django.db import models

# Create your models here.
class NewsSource(models.Model):
    name = models.CharField(max_length=255)
    rss_url = models.URLField(max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Article(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=500,unique=True)
    published = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published',]
        

class Digest(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DigestArticle(models.Model):
    digest = models.ForeignKey(Digest, on_delete=models.CASCADE, related_name='digest_articles')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='+')

    class Meta:
        unique_together = ('digest', 'article')
