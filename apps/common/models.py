from django.db import models
import uuid
from autoslug import AutoSlugField

class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract= True


def _slugify_name_(self):
    return f"{self.name}"

class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from=_slugify_name_, always_update=True, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name