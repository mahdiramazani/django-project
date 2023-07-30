from django import forms
from . models import NewsModels,Comment

class NormalUserPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =("user",)

class AdminUserPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"