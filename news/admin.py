from django.contrib import admin

# Register your models here.
from .models import NewsSource, Article, Digest, DigestArticle

class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'rss_url', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'rss_url')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'source', 'published', 'link')
    search_fields = ('title', 'link')
    list_filter = ('source',)
    ordering = ('-published',)



class DigestAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at')
    search_fields = ('name',)


class DigestArticleAdmin(admin.ModelAdmin):
    list_display = ('digest', 'article')
    list_filter = ('digest',)

admin.site.register(NewsSource, NewsSourceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(DigestArticle, DigestArticleAdmin)
admin.site.register(Digest, DigestAdmin)

