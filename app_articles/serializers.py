from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章序列化器
    将文章模型数据转换为 JSON 格式，或将 JSON 数据验证并转换为模型实例
    """
    # 只读字段：通过 source 参数从关联模型中获取作者用户名
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        # 指定序列化的模型类
        model = Article
        # 指定需要序列化的字段
        fields = [
            'id',
            'title',
            'content',
            'create_time',
            'author_username',
        ]
        # 指定只读字段（客户端无法修改这些字段）
        read_only_fields = [
            'id',
            'create_time',
            'author_username',
        ]
