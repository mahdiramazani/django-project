from django import forms
from . models import User

class NormalUserPostForm(forms.ModelForm):
    class Meta:
        model = User
        fields =("fullname",)

class AdminUserPostForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"