from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializers import (
    CategoryDetailSerializer, PostSerializer, PostDetailSerializer,
    CategorySerializer, CategoryDetailSerializer
)


#
# @api_view()
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts, many=True)
#     return Response(post_serializers.data)
#
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer  # 配置好用来序列化的 serializer = PostSerial zer ，就可以实现一个数据列表页


# class PostViewSet(viewsets.ModelViewSet):
#     """apis.py中PostViewSet文档字符串"""
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     # permission_classes = [IsAdminUser]  # 写入时的权限校验

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """文章Post相关接口"""
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """分类Category相关接口"""
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)