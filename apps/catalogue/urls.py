from django.urls import path 

from .views import (
    PhotoListView, 
    PhotoDetalView,
    VideosListView,
    TagDetailView
    )

urlpatterns = [
    path("", PhotoListView.as_view(), name="photos"),
    path("photo/<id>/", PhotoDetalView.as_view(), name="photo-detail"),

    path("videos/", VideosListView.as_view(), name="videos"),

    path("tag/<id>", TagDetailView.as_view(), name="tag-detail")
]