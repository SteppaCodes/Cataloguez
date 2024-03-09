from django import forms

from .models import Photo, Video

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["title", "description", "img", "tags"]



class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "description", "vid", "tags"]