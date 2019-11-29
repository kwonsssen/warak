from django.urls import path
from . import views

app_name='notice'
urlpatterns =[
    path('',views.notice, name="index"),
    path('<int:pk>/',views.notice_detail, name="detail")
]