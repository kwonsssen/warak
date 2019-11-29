from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .forms import SignUpModelForm
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    context={}
    program_list = models.Program.objects.all()

    context['form']         = SignUpModelForm()
    context['program_list'] = program_list
    return render(request, 'program/program.html',context)

def get_ajax_data(form_data_list):
    data ={}
    for field in form_data_list:
        data[field["name"]] = field["value"]
    return data

def signup(request, pk):
    


    if request.method == "POST":
        for item in request.POST:
            #값이 비어있는게 1개라도 있는지 있다면 에러 메시지 리턴
            if not request.POST.get(item):
                messages.error(request, "모든 빈칸을 채워주세요")
                return redirect('program:index')
        program = models.Program.objects.filter(pk=pk).first()
        print(program)
        qs = models.Program.objects.all()
        qs2 = qs.filter(title__icontains=program)
        for i in qs2:
            print(i.volunteer)
            post = models.Program.objects.get(id=i.id)
            post.volunteer = i.volunteer + 1
            post.save()

        if not program:
            messages.error(request, "유효한 프로그램이 아닙니다.")
            return redirect('program:index')
        print(request.POST.get('gender'))
        print(request.POST)
        models.ProgramSignUp.objects.create(
            program = program,
            name = request.POST.get('student_name'),
            school = request.POST.get('student_school'),
            school_year = request.POST.get('student_level'),
            gender = request.POST.get('gender'),
            email = request.POST.get('student_email'),
            contact = request.POST.get('student_contact'),
            guardian_name = request.POST.get('guardian_name'),
            guardian_contact = request.POST.get('guardian_contact'),
            #email = request.POST.get('email'),
        )
        messages.success(request, "신청이 완료되었습니다.")    
        return redirect('program:index')
# ajax 소스
# def signup(request,pk):
#     context={}
#     if request.is_ajax:
#         data = get_ajax_data(json.loads(request.POST.get('formData')))
#         form = SignUpModelForm(data)
#         if form.is_valid():
#             tmp = form.save(commit=False)
#             tmp.program = models.Program.objects.filter(pk=pk).first()
#             tmp.save()
#             context['result'] = True
#             return JsonResponse(context)
#         else:
#             context['result'] = False
#             context['errors'] = form.errors
#             print(form.errors)
#             return JsonResponse(context)
   