from django.contrib import admin

from typeidea.custom_site import custom_site
from .models import Comment


# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    """后台展示，评论栏入口"""
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
