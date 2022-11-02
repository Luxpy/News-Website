from django.contrib import admin

from apps.articles.models import Article, ArticleAssets


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article


@admin.register(ArticleAssets)
class ArticleAssetsAdmin(admin.ModelAdmin):
    model = ArticleAssets
