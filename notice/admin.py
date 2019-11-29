from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_per_page=5
    list_display=(
        'title',
        'created_at',
    )
    search_fields=('title',)
    ordering =(
        'title',
        'created_at',
    )