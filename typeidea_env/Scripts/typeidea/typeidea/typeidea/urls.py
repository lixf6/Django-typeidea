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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

# from blog.views import post_list, post_detail
from config.views import links
from .custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView, PostDetailView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 访问首页
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),  # 分类列表页
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),  # 标签列表页
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),  # 博客详情页
    url(r'^links/$', links, name='links'),  # 友链展示页
    url(r'^super_admin/', admin.site.urls, name='super-admin'),  # 用户、权限后台
    url(r'^admin/', custom_site.urls, name='admin'),  # 文章、分类、标签后台
]
