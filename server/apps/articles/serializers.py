from rest_framework import serializers

from apps.articles.models import Article, ArticleAssets


class ArticleSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ["author", "number_likes"]


class ArticleAssetsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAssets
        fields = "__all__"
