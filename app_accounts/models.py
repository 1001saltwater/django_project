from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    用户资料模型
    扩展 Django 默认用户模型，存储用户额外信息
    通过 OneToOneField 与 User 模型关联，实现一对一关系
    """
    # 与 Django 默认用户模型建立一对一关系
    # on_delete=models.CASCADE: 当用户被删除时，资料也随之删除
    # related_name='userprofile': 允许通过 user.userprofile 访问用户资料
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile',
        verbose_name="用户"
    )
    # 用户昵称，最大长度20，可为空
    nickname = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="昵称"
    )
    # 用户头像，上传至 avatars/ 目录，可为空
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="头像"
    )
    # 用户简介/个人描述，可为空
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="个人简介"
    )
    # 创建时间，自动填充当前时间
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )

    class Meta:
        verbose_name = "用户资料"
        verbose_name_plural = "用户资料"

    def __str__(self):
        """返回用户的用户名作为模型的字符串表示"""
        return self.user.username
