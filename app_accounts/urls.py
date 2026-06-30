from django.urls import path
from . import views

urlpatterns = [
    # 用户资料接口
    # GET /api/profile/     获取当前用户资料（需登录）
    # PUT /api/profile/     完整更新当前用户资料（需登录）
    # PATCH /api/profile/   部分更新当前用户资料（需登录）
    path("profile/", views.UserProfileView.as_view()),
]
