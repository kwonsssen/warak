from django.urls import path
from . import views

app_name='apply'
urlpatterns =[
    path('mento/', views.mento, name='mento'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('work/', views.workexp, name='work'),
]