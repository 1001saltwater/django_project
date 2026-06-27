from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'create_time',
            'author_username',
        ]
        read_only_fields = [
            'id',
            'create_time',
            'author_username',
        ]
