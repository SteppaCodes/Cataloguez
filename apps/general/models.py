from django.db import models
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError

from apps.common.models import BaseModel

class SiteDetail(BaseModel):
    name = models.CharField(max_length=300)
    desc = models.TextField(_("description"), null=True)
    email = models.EmailField()
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=20, null =True)
    website = models.URLField(default="https://cataloguez.com")
    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    ig = models.URLField(
        verbose_name=_("Instagram"), default="https://www.instagram.com/"
    )
    x = models.URLField(verbose_name=_("X"), default="https://www.X.com/")
    pt = models.URLField(
        verbose_name=_("Pinterest"), default="https://www.pinterest.com/"
    )
    maps_url = models.URLField(default="https://maps.google.com/maps?q=Av.+L%C3%BAcio+Costa,+Rio+de+Janeiro+-+RJ,+Brazil&t=&z=13&ie=UTF8&iwloc=&output=embed")

    def save(self, *arg, **Kwargs):
        if self._state.adding and SiteDetail.objects.exists():
            raise ValidationError(_("Only one sitedetail object can be created"))
        return super(SiteDetail, self).save(*arg, **Kwargs)

    def __str__(self):
        return self.name
    

ROLE_CHOICES = (
    ("Chief Executive Officer", "Chief Executive Officer"),
    ("Chief Marketing Officer", "Chief Marketing Officer"),
    ("Accounting Executive", "Accounting Executive"),
    ("Creative Art Director #C69", "Creative Art Director #C69"),
)


class TeamMember(BaseModel):
    name= models.CharField(max_length=100)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
    desc= models.TextField(_("description"))
    vision = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
    avatar= models.ImageField(upload_to='team/')
    
    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    x = models.URLField(verbose_name=_("X"), default="https://www.X.com/")
    ln = models.URLField(
        verbose_name=_("Linkedin"), default="https://www.linkedin.com/"
    )

    def __str__(self):
        return self.name
    
    @property
    def get_avatar(self):
        try:
            url=self.avatar.url
        except:
            url=''
        return url

class Subject(BaseModel):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Message(BaseModel):
    name=models.CharField(max_length=300)
    email=models.EmailField()
    subject= models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    text = models.TextField()

    def __str__(self):
        return self.name


