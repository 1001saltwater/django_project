from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    所有人可读；只有文章作者可修改或删除。
    """

    def has_object_permission(self, request, view, obj):
        # GET / HEAD / OPTIONS
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user