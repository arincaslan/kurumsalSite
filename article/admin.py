from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('article_slug',)
admin.site.register(Article, ArticleAdmin)
