from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Article(models.Model):
    """
    文章模型
    用于存储博客文章的基本信息
    """
    title = models.CharField(max_length=100, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name="作者"
    )

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ["-create_time"]

    def __str__(self):
        return self.title
