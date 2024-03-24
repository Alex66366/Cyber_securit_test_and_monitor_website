from django.shortcuts import render
from regist.models import Normal_Person,Super_Person
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
import re

# Create your views here.
#普通用户页面
def UserLogin_page(request):
    if request.method == "GET":
        return render(request,'UserLogin.html')

#超级管理员页面
def Super_UserLogin_page(request):
    # if request.method =="GET":
    return render(request,'ManagerLogin.html')

#注册页面
def Reister_page(request):
    if request.method =="GET":
        return render(request,'Register.html')

def Main_page(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        return render(request,'index.html',{'user_id':user_id})
    else:
        return render(request,'NotLogin.html')

#检验用户名和密码
def check_normal_person(request):
    if request.method=='POST':
        user_id_check = request.POST.get('user_id')
        password_check = request.POST.get('password')
        if len(user_id_check)==0 or len(password_check)==0:
            return HttpResponse("Empty")
        user_id_exist = Normal_Person.objects.filter(user_id = user_id_check, password = password_check)
        if user_id_exist.exists():
            request.session['user_id'] = user_id_check
            request.session['password'] = password_check
            return HttpResponse("Success")
        else:
            return HttpResponse("Wrong")
    else:
        return HttpResponse("Method Error")

def check_super_person(request):
    if request.method=='POST':
        user_id_check = request.POST.get('user_id')
        password_check = request.POST.get('password')
        print(user_id_check)
        print(password_check)
        if len(user_id_check)==0 or len(password_check)==0:
            return HttpResponse("Empty")
        user_id_exist = Super_Person.objects.filter(user_id = user_id_check, password = password_check)
        if user_id_exist.exists():
            request.session['user_id'] = user_id_check
            request.session['password'] = password_check
            return HttpResponse("Success")
        else:
            return HttpResponse("Wrong")
    else:
        return HttpResponse("Method Error")


