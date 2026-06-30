from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    自定义权限类：文章作者权限
    所有用户均可查看文章（GET/HEAD/OPTIONS 请求），
    但只有文章作者可以修改或删除文章（POST/PUT/PATCH/DELETE 请求）。
    """

    def has_object_permission(self, request, view, obj):
        """
        判断当前用户是否有操作该对象的权限
        :param request: 请求对象
        :param view: 视图对象
        :param obj: 要操作的对象（文章实例）
        :return: 是否有权限
        """
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        # 安全请求方法：允许所有用户访问
        if request.method in SAFE_METHODS:
            return True

        # 非安全请求方法：仅作者可操作
        return obj.author == request.user
