from django.shortcuts import render,redirect
from django.contrib import messages
from . import models

#객체 생성
def apply(obj,data):
    obj.objects.create(
        name = data.get('name'),
        telephone = data.get('telephone'),
        schoolinfo = data.get('schoolinfo'),
        email = data.get('email'),
        content = data.get('content'),
        info_agree = 1
    )
    return True

#폼 빈칸 찾기 및 
def check_validation(request):
    for item in request.POST:
        #값이 비어있는게 1개라도 있는지 있다면 에러 메시지 리턴
        if not request.POST.get(item):
            messages.error(request, "모든 빈칸을 채워주세요")
            return False
    #동의 하지 않는다면 false가 리턴되므로
    if not request.POST.get('info_agree'):
        messages.error(request, "하단의 개인정보 동의가 필요합니다.")
        return False
    return True

#멘토 신청
def mento(request, context={'title':'멘토'}):
    context['is_page']=1
    if request.method == 'POST':
        if check_validation(request):
            if apply(models.Mento, request.POST):
                messages.success(request, "등록이 완료되었습니다.")
    context['static_photo'] = 'img/apply/apply1.jpg'
    return render(request,'apply/apply.html',context)


#봉사신청
def volunteer(request,context={'title':'자원봉사'}):
    context['is_page']=2
    if request.method == 'POST':
        if check_validation(request):
            if apply(models.Volunteer, request.POST):
                messages.success(request, "신청이 완료되었습니다.")
    context['static_photo'] = 'img/apply/apply2.jpg'
    return render(request,'apply/apply.html',context)

#봉사신청
def workexp(request,context={'title':'직업체험일터'}):
    context['is_page']=3
    if request.method == 'POST':
        if check_validation(request):
            if apply(models.WorkExp, request.POST):
                messages.success(request, "신청이 완료되었습니다.")
    context['static_photo'] = 'img/apply/apply3.jpg'
    return render(request,'apply/apply.html',context)