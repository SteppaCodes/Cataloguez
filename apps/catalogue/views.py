from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Photo, Video, Tag
from .forms import PhotoForm, VideoForm


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


class UploadMediaRequestView(View):
   def get(self, request):
        return render(request, 'catalogue/upload-type.html')



class UploadMediaView(View):
    def get(self, request, type):
        
        if type == "photo":
            form = PhotoForm()
        else:
            form = VideoForm()

        context = {
            "form":form
        }
        return render(request, 'catalogue/upload-media.html', context)
    
    def post(self, request, type):
        if type == "photo":
            form = PhotoForm(request.POST, request.FILES)
        else:
            form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            media = form.save(commit=False)
            media.user = request.user
            print(media.img)
            media.save()
            
            media.tags.set(form.cleaned_data['tags'])
            return redirect('photos')

        context = {
            "form":form
        }
        return render(request, 'catalogue/upload-media.html', context)
