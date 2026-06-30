from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    用户资料管理后台配置
    自定义 Django 管理后台中用户资料模型的显示和操作
    """
    # 列表页显示的字段
    list_display = ('user', 'nickname', 'create_time')
    # 列表页可搜索的字段
    search_fields = ('user__username', 'nickname', 'bio')
    # 列表页过滤条件
    list_filter = ('create_time',)
    # 详情页字段分组
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('个人信息', {
            'fields': ('nickname', 'avatar', 'bio'),
        }),
    )
