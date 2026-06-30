from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    文章管理后台配置
    自定义 Django 管理后台中文章模型的显示和操作
    """
    # 列表页显示的字段
    list_display = ('title', 'author', 'create_time')
    # 列表页可搜索的字段
    search_fields = ('title', 'content', 'author__username')
    # 列表页过滤条件
    list_filter = ('author', 'create_time')
    # 详情页字段分组
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('作者信息', {
            'fields': ('author',),
            'classes': ('collapse',)
        }),
    )
