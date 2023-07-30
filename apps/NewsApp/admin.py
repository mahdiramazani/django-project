from django.contrib import admin
from .models import NewsModels,Category,Comment,ImageGallery
from . import forms

admin.site.register(ImageGallery)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user","body"]
    search_fields = ["body"]
    form = forms.NormalUserPostForm



    # Staff can't add site announcements
    def has_add_permission(self, request):
        if not request.user.is_admin:
            return False
        return True

    # Staff can't edit site announcements
    def has_change_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True

    # Staff can't delete site announcements
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]




    # def get_readonly_fields(self, request, obj=None):
    #     if not request.user.is_admin:
    #         return 'title','body'
    #     return super(CommentAdmin, self).get_readonly_fields(request)


    # Staff can't add site announcements
    def has_add_permission(self, request):
        if not request.user.is_admin:
            return False
        return True

    # Staff can't edit site announcements
    def has_change_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True

    # Staff can't delete site announcements
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True


@admin.register(NewsModels)
class AdminNews(admin.ModelAdmin):
    list_display = ["title", "writer","writer_guild"]
    search_fields = ["title"]

    def get_readonly_fields(self, request, obj=None):
        if  not (request.user.is_admin  or   request.user.is_publishing_news):
            return 'title','body'
        else:
            return super(AdminNews, self).get_readonly_fields(request)

    # Staff can't add site announcements
    def has_add_permission(self, request):
        if  not (request.user.is_admin  or   request.user.is_publishing_news):
            return False
        else:
            return True

    # Staff can't edit site announcements
    def has_change_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True

    # Staff can't delete site announcements
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True

