from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from blog.views import CommonViewMixin
from .models import Link


# Create your views here.
class LinkListView(CommonViewMixin, ListView):
    """前端展示，友链展示入口"""
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
    # return HttpResponse('links')


# def links(request):
#     """前端展示，友链展示入口"""
#     return HttpResponse('links')