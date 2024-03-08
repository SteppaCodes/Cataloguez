from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Photo, Video, Tag


class PhotoListView(View):
    def get(self, request):
        photos = Photo.objects.all()

        context = {
            "photos": photos
        }
        return render(request, "catalogue/photos.html", context)


class PhotoDetalView(View):
    def get(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        tags = photo.tags.all()

        context = {
            'photo':photo,
            "tags":tags
        }
        return render(request, "catalogue/photo-detail.html", context)


class VideosListView(View):
    def get(self, request):
        videos = Video.objects.all()


        context = {
            'videos':videos
        }
        return render(request, "catalogue/videos.html", context)


class TagDetailView(View):
    def get(self, request, id):
        tag = get_object_or_404(Tag, id=id)
        #fix this
        photos = Photo.objects.filter(tags=tag)
        videos = Video.objects.filter(tags=tag)


        context = {
            "tag":tag,
            "photos":photos,
            "videos":videos
        }
        return render(request, 'catalogue/tag-medias.html', context)
