from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# 创建默认路由器实例
router = DefaultRouter()
# 注册文章视图集，路由前缀为 'articles'
# 自动生成以下路由：
# - GET /api/articles/          获取文章列表
# - POST /api/articles/         创建新文章
# - GET /api/articles/<pk>/     获取单篇文章
# - PUT /api/articles/<pk>/     更新文章
# - PATCH /api/articles/<pk>/   部分更新文章
# - DELETE /api/articles/<pk>/  删除文章
router.register("articles", views.ArticleViewSet)

urlpatterns = [
    # 将路由器生成的所有路由包含进来
    path("", include(router.urls)),
]
