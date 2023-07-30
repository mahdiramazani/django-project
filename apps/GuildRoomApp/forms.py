from django import forms
from . models import GuildRoomModel

class NormalUserPostForm(forms.ModelForm):
    class Meta:
        model = GuildRoomModel
        fields =("name",)

class AdminUserPostForm(forms.ModelForm):
    class Meta:
        model = GuildRoomModel
        fields = "__all__"