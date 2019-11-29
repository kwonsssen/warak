from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    context={'gallery_list':models.Gallery.objects.all()}
    return render(request, 'gallery/gallery.html',context)