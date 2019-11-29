from django.contrib import admin
from . import models


@admin.register(models.Mento)
class MentoAdmin(admin.ModelAdmin):
    list_per_page= 5
    list_display=(
        'name', 'telephone', 'schoolinfo','email', 'info_agree', 'created_at'
    )
    search_fields=('name',)
    ordering =(
        'name',
        'email',
        'created_at',
    )

@admin.register(models.Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_per_page= 5
    list_display=(
        'name', 'telephone', 'schoolinfo','email', 'info_agree','created_at'
    )
    search_fields=('name',)
    ordering =(
        'name',
        'email',
        'created_at',
    )                                                           
@admin.register(models.WorkExp)
class WorkExpAdmin(admin.ModelAdmin):
    list_per_page= 5
    list_display=(
        'name', 'telephone', 'schoolinfo','email', 'info_agree', 'created_at'
    )
    search_fields=('name',)
    ordering =(
        'name',
        'email',
        'created_at',
    )                                                           
