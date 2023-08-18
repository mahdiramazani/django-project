from django.contrib import admin
from .models import GuildRoomModel,CommissionsModel
from . import forms

admin.site.site_header = 'مدیریت وبسایت اتاق اصناف سیرجان'
admin.site.register(GuildRoomModel)
admin.site.register(CommissionsModel)
# @admin.register(GuildRoomModel)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ["name","slug"]
#     search_fields = ["name"]
#     form = forms.NormalUserPostForm
#
#
#     def has_add_permission(self, request):
#         if not request.user.is_admin:
#             return False
#         return True
#
#     # Staff can't edit site announcements
#     def has_change_permission(self, request, obj=None):
#         if not request.user.is_admin:
#             return False
#         return True
#
#     # Staff can't delete site announcements
#     def has_delete_permission(self, request, obj=None):
#         if not request.user.is_admin:
#             return False
#         return True
