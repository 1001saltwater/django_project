from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    用户资料序列化器
    将用户资料模型数据转换为 JSON 格式，或将 JSON 数据验证并转换为模型实例
    用于用户资料的查询和修改操作
    """
    class Meta:
        # 指定序列化的模型类
        model = UserProfile
        # 指定需要序列化的字段
        # 客户端可修改的字段：昵称、头像、个人简介
        fields = [
            "nickname",
            "avatar",
            "bio",
        ]
