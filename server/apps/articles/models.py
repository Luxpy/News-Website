from django.db import models
from django.contrib.auth import get_user_model

from tinymce.models import HTMLField

UserModel = get_user_model()


def get_article_upload_path(instance, filename):
    return "/".join(["images", "articles", instance.id, filename])


def get_assets_upload_path(instance, filename):
    return "/".join(["assets", "articles", instance.article.id, filename])


class Article(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    title = models.CharField(max_length=60)
    image = models.ImageField(
        upload_to=get_article_upload_path,
        default="images/defaults/article-default.png"
    )
    body = HTMLField()
    number_likes = models.PositiveSmallIntegerField(default=0)

    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)


class ArticleAssets(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    file = models.FileField(upload_to=get_assets_upload_path)
