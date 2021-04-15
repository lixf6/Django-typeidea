from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def links(request):
    """前端展示，友链展示入口"""
    return HttpResponse('links')