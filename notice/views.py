from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models

def get_pagination(model,name ,bundle, page,):
    context={}

    model_page = Paginator(model, bundle)
    page_range= 5
    max_index= len(model_page.page_range)
    current_page = int(page)
    start_index = int((current_page-1 ) / page_range) * page_range
    end_index = start_index + page_range
    if end_index >= max_index:
        end_index = max_index

    page_range = model_page.page_range[start_index:end_index]

    try:
        model_page = model_page.get_page(page)
    except PageNotAnInteger:
        model_page = model_page.page(1)
    except EmptyPage:
        model_page = model_page.page(model_page.num_pages)

    context[name]= model_page
    context['page_range'] = page_range
    context['max_index'] = max_index
    return context

def notice(request):
    context={}
    notice_list = models.Notice.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    context = get_pagination(notice_list,'notice_page',10,page)
    return render(request,'notice/notice.html',context)

def notice_detail(request,pk):
    notice = get_object_or_404(models.Notice,pk=pk)
    return render(request, 'notice/notice-detail.html',{'notice':notice})