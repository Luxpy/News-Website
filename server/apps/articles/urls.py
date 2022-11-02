from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.articles.views import ArticleViewSet, ArticleAssetsCreateAPIView

articleRouter = SimpleRouter()
articleRouter.register(r'articles', ArticleViewSet, 'articles')

urlpatterns = [
    path('', include(articleRouter.urls)),
    path('articles-assets/create/', ArticleAssetsCreateAPIView.as_view(), name='article-assets-create')
]
