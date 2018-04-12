from django.shortcuts import render
from .models import *
from .task import *
from django.http import HttpResponse

def text(request):
    return render(request,'booktest/text.html')

def show(request):
    data = request.POST['hcontent']
    test = Test()
    test.content = data
    test.save()

    context = {'data':data}
    return render(request,'booktest/show.html',context)

# 全文索引
def set(request):
    return render(request,'booktest/set.html')

# 使用celery
def show_test(request):
    #show_()
    show_.delay()
    return  HttpResponse('ok')

