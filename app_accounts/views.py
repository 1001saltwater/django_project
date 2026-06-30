from rest_framework.views import APIView
from rest_framework.response import Response
from logging import Logger
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
import logging

# 获取当前模块的日志记录器
logger = logging.getLogger(__name__)


class UserProfileView(APIView):
    """
    用户资料视图
    提供当前登录用户的资料查询和修改功能
    需要用户登录认证（IsAuthenticated）
    """
    # 权限类：仅登录用户可访问
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        获取当前用户的资料
        :param request: 请求对象
        :return: 用户资料序列化数据
        """
        # 调试日志：记录当前用户信息（可在生产环境中移除）
        logger.debug(self, request.user)
        logger.debug(self, type(request.user))
        
        # 通过 related_name 获取用户关联的资料对象
        profile = request.user.userprofile
        # 序列化资料对象
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        """
        完整更新当前用户的资料
        :param request: 请求对象，包含更新的数据
        :return: 更新后的用户资料或错误信息
        """
        profile = request.user.userprofile
        # 使用传入的数据完整更新资料（所有字段必须提供）
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # 验证失败，返回错误信息和 400 状态码
            return Response(serializer.errors, status=400)

    def patch(self, request):
        """
        部分更新当前用户的资料
        :param request: 请求对象，包含部分更新的数据
        :return: 更新后的用户资料或错误信息
        """
        profile = request.user.userprofile
        # 使用传入的数据部分更新资料（只需提供要修改的字段）
        # partial=True 参数允许部分更新
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
