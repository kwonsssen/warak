from django.urls import path
from . import views

app_name='program'

urlpatterns =[
    path('', views.index, name="index"),
    path('<int:pk>/',views.signup, name="signup"),
]