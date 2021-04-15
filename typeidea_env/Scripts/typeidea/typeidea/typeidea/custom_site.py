from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    """后台admin设置顶部部分字段展示"""
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'

# 实例化CustomSite
custom_site = CustomSite(name='cus_admin')