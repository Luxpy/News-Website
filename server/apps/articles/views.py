from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from apps.articles.models import Article, ArticleAssets
from apps.articles.serializers import ArticleSerialzer, ArticleAssetsSerialzer
from apps.articles.permission import IsAuthorOrReadOnly, IsAssetsAuthorOrReadOnly


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialzer
    permission_classes = (IsAuthorOrReadOnly, )


class ArticleAssetsCreateAPIView(CreateAPIView):
    queryset = ArticleAssets.objects.all()
    serializer_class = ArticleAssetsSerialzer
    permission_classes = (IsAssetsAuthorOrReadOnly, )
