from django.shortcuts import render
from register.models import Normal_Person
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render,HttpResponse

#登录页面的整体框架
# def background_page(request):
#     if request.method == "GET":
#         return render(request,'0.html')

#检验用户名和密码
def check1(request):
    if request.method=='POST':
        user_id_check = request.POST.get('user_id')
        password_check = request.POST.get('password')
        user_id_exist = Normal_Person.objects.filter(user_id = user_id_check,password = password_check)
        if not user_id_exist:
            return JsonResponse("Wrong")
        else:
            return JsonResponse("Success")
    else:
        return "Method Error"



