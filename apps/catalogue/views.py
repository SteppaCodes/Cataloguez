from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import FileResponse
from django.db.models import Q

from .models import Photo, Video, Tag
from .forms import PhotoForm, VideoForm
from apps.accounts.mixins import LoginRequiredMixin

import sweetify
import requests
import cloudinary


def _get_format_(request, key):
        # Acces the file
        file = request.FILES
        # Get the file name
        name = file[key].name
        # Split the nmme where theres a . and get the value of the index 1 (this should contain the file format)
        format = name.split(".")[1]
        return format

def _get_media_file_(id):
    try:
        file = Photo.objects.get(id=id)
        media = "img"
        return file, media
    except Photo.DoesNotExist:
        try:
            file = Video.objects.get(id=id)
            return file
        except Video.DoesNotExist:
            return None


class PhotoListView(ListView):
    model = Photo
    paginate_by = 10
    template_name = 'catalogue/photos.html'
    context_object_name = 'photos'

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(
                Q(title__icontains=query)
            )
        return qs


class PhotoDetalView(View):
    def get(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        photo.views += 1
        photo.save()
        tags = photo.tags.all()

        # Create a list of the id of all the tags used in the photo
        photo_tag_ids = tags.values_list('id', flat=True)
        # Get all photos that have the tags in the photo_tag_ids list excluding the photo itself
        related_photos = Photo.objects.filter(tags__in=photo_tag_ids).exclude(id=id).distinct()
        # Count the number of tags that are the same in similar photos and return them from highest to lowest
        related_photos = related_photos.annotate(same_tags=Count('tags')).order_by('-same_tags')


        context = {
            'photo':photo,
            "tags":tags,
            "related_photos": related_photos
        }
        return render(request, "catalogue/photo-detail.html", context)


class VideosListView(ListView):
    model = Video
    paginate_by = 10
    template_name = 'catalogue/videos.html'
    context_object_name = 'videos'


class TagDetailView(View):
    def get(self, request, id):
        tag = get_object_or_404(Tag, id=id)
        #fix this
        photos = Photo.objects.filter(tags=tag)
        videos = Video.objects.filter(tags=tag)
        media_count = photos.count() + videos.count()

        context = {
            "tag":tag,
            "photos":photos,
            "videos":videos,
            "count":media_count
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
            format = _get_format_(request=request, key="img")
        else:
            form = VideoForm(request.POST, request.FILES)
            format = _get_format_(request=request, key="vid")

        if form.is_valid():
            media = form.save(commit=False)
            media.user = request.user
            media.format=format
            media.save()
            sweetify.success(request, 
                             title="sent",
                             text="Your Message was sent successfully",
                             timer=300000
            )
            # create the manytomany relationship for each tag selected
            media.tags.set(form.cleaned_data['tags'])
            return redirect('photos')

        context = {
            "form":form
        }
        return render(request, 'catalogue/upload-media.html', context)


class DownloadMediaView(View, LoginRequiredMixin):
    def get(self, request, id):
        file, media = _get_media_file_(id=id)

        
        
        if file:
            file_url = file.image_url if media == "img" else file.video_url
            
            # Fetch the file from Cloudinary
            response = cloudinary.api.download(file_url)
            
            # Set the appropriate content disposition for downloading
            response["Content-Disposition"] = f'attachment; filename="{file.file.name}"'
            
            # Return the file as a response
            return response
            
        # Handle the case where file is not found
        raise FileNotFoundError("File not found")    


