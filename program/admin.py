from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_per_page= 5
    list_display=(
        'title',
        'classify',
        'target',
        'schedule',
        'signup_day',
    )
    search_fields=('title','classify')
    ordering =(
        'title',
        'classify',
        'target',
    )
    
    def schedule(self,obj):
        return '{} . {} . {} ~ {} . {} . {}'.format(
            obj.start_schedule.year,
            obj.start_schedule.month,
            obj.start_schedule.day,
            obj.end_schedule.year,
            obj.end_schedule.month,
            obj.end_schedule.day
        )
    
    def signup_day(self,obj):
        return '{} . {} . {} ~ {} . {} . {}'.format(
            obj.start_signup_day.year,
            obj.start_signup_day.month,
            obj.start_signup_day.day,
            obj.end_signup_day.year,
            obj.end_signup_day.month,
            obj.end_signup_day.day
        )
    
    schedule.short_description = '일정'
    signup_day.short_description = '신청기간'



@admin.register(models.ProgramSignUp)
class ProgramSignUpAdmin(admin.ModelAdmin):
    list_per_page= 5
    list_display=(
        'program',
        'guardian_name',
        'guardian_contact',
        'name',
        'gender',
        'email',
        'contact',
        'school',
        'created_at',
    )
    search_fields=('guardian_name','name')