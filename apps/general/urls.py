from django.urls import path
from .views import AboutPageView, ContactPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),

]
