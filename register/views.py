from django.shortcuts import render
from .models import Normal_Person
from django.http import JsonResponse
# Create your views here.

#注册
def user_regist(request):
    if request.method =='POST':
        get_user_id = request.POST.get('user_id')
        exist_user_id = Normal_Person.objects.filter(user_id = get_user_id)
        if not exist_user_id:
            return JsonResponse("Success")
        else:
            return JsonResponse("Fail")
    else:
        return JsonResponse("Method Error")
