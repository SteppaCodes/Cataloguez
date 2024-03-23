from .models import Photo, Video

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
