from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.contrib.sites import requests
from django.urls import reverse
from django.utils.html import format_html

from typeidea.custom_site import custom_site

from typeidea.base_admin import BaseOwnerAdmin
from .adminforms import PostAdminForm
from .models import Post, Category, Tag
from django.contrib.admin.models import LogEntry


# PERMISSION_API = "http://127.0.0.1:5000/200"


class PostInline(admin.TabularInline):
    # 在目录页面新增对文章发布的关联控制
    fields = ('title', 'desc')
    extra = 1
    model = Post


# Register your models here.
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    """后台分类设置栏，admin/路径下"""
    # inlines = [PostInline, ]
    # list_display 分类列表页字段展示
    list_display = ('name', 'status', 'is_nav', 'created_time', 'owner', 'post_count')
    # fields 修改或新建分类页时，页面展示的字段
    fields = ('name', 'status', 'is_nav')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        """文章总数计数返回"""
        return obj.post_set.count()

    # 列表展示字段，该目录下对应文章字段展示名称
    post_count.short_description = "文章数量"


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        """返回要展示的内容和查询用的 id"""
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        """这里 QuerySet表页所有展示数据的合集，即 post的数据集"""
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    """后台标签设置栏，admin/路径下"""
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    """后台文章设置栏，admin/路径下"""
    # 使用摘要多行展示设置
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status', 'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    # list_filter = ['category', ]
    # 使用自定义过滤器，只展示当前用户分类
    list_filter = [CategoryOwnerFilter, ]
    # 搜索栏中支持搜索字段
    search_fields = ['title', 'category_name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    exclude = ['owner']
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),

        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),

        ('额外信息', {
            'classes': ('wide',),  # wide  collapse
            'fields': (
                'tag',
            ),
        })
    )

    # 标签栏字段展示方式，这里为水平放置
    filter_horizontal = ('tag',)
    # filter_vertical = ('tag',)

    # 操作字段设置
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    # 继承bootstrap样式
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)

    # def has_add_permission(self, request):
    #     opts = self.opts
    #     codename = get_permission_codename('add', opts)
    #     perm_code = "%s.%s" % (opts.app_label, codename)
    #     resp = requests.get(PERMISSION_API.format(request.user.username, perm_code))
    #     if resp.status_code == 200:
    #         return True
    #     else:
    #         return False

@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    """后台展示日志入口，对应admin/路径下"""
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']