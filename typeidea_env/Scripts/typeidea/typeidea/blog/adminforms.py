from django import forms


class PostAdminForm(forms.ModelForm):
    """后台摘要字段从单行展示变成多行展示"""
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)