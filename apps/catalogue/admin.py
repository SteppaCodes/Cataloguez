from django.contrib import admin
from .models import Photo, Video


class PhotoAdmmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at", "updated_at"]
    list_filter = list_display


class VideoAdmmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at", "updated_at"]
    list_filter = list_display


admin.site.register(Photo, PhotoAdmmin)
admin.site.register(Video, VideoAdmmin)

