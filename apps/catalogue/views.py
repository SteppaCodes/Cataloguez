from django.shortcuts import render
from django.views import View


class PhotoListView(View):
    def get(self, request):
        return render(request, "catalogue/photos.html")


