from django.db import models

from apps.common.models import BaseModel, Tag
from apps.accounts.models import User

class CatalogueBaseModel(BaseModel):
    title = models.CharField(max_length=300)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True


class Photo(CatalogueBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    img = models.ImageField(upload_to='images/')

    def  __str__(self):
        return self.title

    @property
    def image_url(self):
        try:
            url = self.img.url
        except:
            url = ""
        return url
    

class Video(CatalogueBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    vid = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
    
    @property
    def video_url(self):
        try:
            url = self.vid.url
        except:
            url = ""
        return url
    
