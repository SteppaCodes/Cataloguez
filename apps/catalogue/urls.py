from django.urls import path 

from .views import (
    PhotoListView, 
    PhotoDetalView,
    VideosListView,
    VideoDetailView,
    TagDetailView,
    UploadMediaRequestView,
    UploadMediaView,
    DownloadMediaView
    )

urlpatterns = [
    path("", PhotoListView.as_view(), name="photos"),
    path("photo/<slug>/", PhotoDetalView.as_view(), name="photo-detail"),

    path("videos/", VideosListView.as_view(), name="videos"),
    path('videos/<slug>/', VideoDetailView.as_view(), name='video-detail'),

    path("tag/<slug>", TagDetailView.as_view(), name="tag-detail"),

    path('upload-media/', UploadMediaRequestView.as_view(), name='upload-request'),
    path('upload/<str:type>', UploadMediaView.as_view(), name='upload'),

    path("download/<slug>/", DownloadMediaView.as_view(), name='download')
]