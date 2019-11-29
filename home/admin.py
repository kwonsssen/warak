from django.contrib import admin
from . import models

@admin.register(models.HomePhoto)
class HomeAdmin(admin.ModelAdmin):
    list_display=(
        'title',
    )
    search_fields=('title',)
    ordering =(
        'title',
    )


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'position',
        'career',
    )
    search_fields=('name',)
    ordering =(
        'position',
        'name',
        'career',
    )
@admin.register(models.PopUp)
class PopUpAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_view',
    )
    search_fields = ('title',)