from django.contrib import admin
from . import models

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=(
        'classify',
        'name',
        'date',
        
    )
    search_fields=('classify',)