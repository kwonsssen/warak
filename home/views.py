from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    photo_list = models.HomePhoto.objects.all()
    employee_list = models.Employee.objects.all()
    context={
        'photo_list':photo_list,
        'employee_list':employee_list,
        }
    context['popup'] = models.PopUp.objects.all().first()
    return render(request,'home/home.html',context)

def popup(request):
    context={
        'popup' : models.PopUp.objects.all().first()
    }
    return render(request,'home/popup.html', context)