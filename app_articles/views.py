from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章视图集
    提供文章的 CRUD 操作：
    - list: 获取文章列表（公开访问）
    - retrieve: 获取单篇文章（公开访问）
    - create: 创建文章（需要登录）
    - update: 更新文章（仅作者可操作）
    - partial_update: 部分更新文章（仅作者可操作）
    - destroy: 删除文章（仅作者可操作）
    """
    # 查询集：预加载作者信息，按创建时间倒序排列
    queryset = Article.objects.select_related("author").order_by("-create_time")
    # 序列化器：用于数据的序列化和反序列化
    serializer_class = ArticleSerializer
    # 权限类：
    # 1. IsAuthenticatedOrReadOnly: 未登录用户只能读取，登录用户可创建
    # 2. IsAuthorOrReadOnly: 仅文章作者可修改/删除
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]

    def perform_create(self, serializer):
        """
        创建文章时自动设置作者为当前登录用户
        重写此方法以在保存前注入额外数据
        """
        serializer.save(author=self.request.user)
