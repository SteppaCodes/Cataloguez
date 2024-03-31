from django.db import models
from cloudinary_storage.storage import VideoMediaCloudinaryStorage

from apps.common.models import BaseModel, Tag
from autoslug import AutoSlugField
from apps.accounts.models import User

def _slugify_title_(self):
    return f"{self.title}"

class CatalogueBaseModel(BaseModel):
    title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from=_slugify_title_, null=True, blank=True, always_update=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    format = models.CharField(max_length= 10, null=True, blank=True)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["-views"]


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
    vid = models.FileField(upload_to='videos/', storage=VideoMediaCloudinaryStorage())
    duration = models.CharField(max_length=20, default='00:00:00')

    def __str__(self):
        return self.title
    
    @property
    def video_url(self):
        try:
            url = self.vid.url
        except:
            url = ""
        return url
    
