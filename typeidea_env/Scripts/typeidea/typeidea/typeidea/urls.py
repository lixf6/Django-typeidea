"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import silk
from django.conf import settings
# from debug_toolbar.panels import settings
from django.conf.urls import url
from django.contrib import admin
# from django.urls import path, include
from django.contrib.sitemaps import views as sitemap_views

# from blog.views import post_list, post_detail
# from config.views import links
from comment.views import CommentView

# from blog.apis import post_list, PostList
from django.urls import include

from .custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView,
)
from config.views import LinkListView
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from blog.apis import PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
# http://127.0.0.1:8000/api/docs/ 中左侧展示控制
router.register(r'category', CategoryViewSet, basename='api-category')

# URL映射：让用户访问 URL 时把数据发送到我们定义的View
urlpatterns = [
    # url(r'^api/post/', post_list, name='post-list'),
    # url(r'^api/post/', PostList.as_view(), name='post-list'),
    url(r'api/docs/', include_docs_urls(title='typeidea apis')),
    url(r'^api/', include((router.urls, 'api'), namespace="api")),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^search/$', SearchView.as_view(), name='search'),  # 首页搜索
    url(r'^$', IndexView.as_view(), name='index'),  # 访问首页
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),  # 分类列表页
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),  # 标签列表页
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),  # 博客详情页
    # url(r'^links/$', links, name='links'),  # 友链展示页
    url(r'^super_admin/', admin.site.urls, name='super-admin'),  # 用户、权限后台
    url(r'^admin/', custom_site.urls, name='admin'),  # 文章、分类、标签后台
]

if settings.DEBUG:
    import debug_toolbar

    # urlpatterns = [
    #                   url(r'^__debug__/', include(debug_toolbar.urls)),
    #               ] + urlpatterns

    urlpatterns = [
                      url(r'^silk/', include('silk.urls', namespace='silk')),
                  ] + urlpatterns