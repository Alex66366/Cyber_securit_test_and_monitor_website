from django.shortcuts import render
from .models import Normal_Person
from django.http import JsonResponse,HttpResponse
from .models import Normal_Person
import re
# Create your views here.

#检验注册
def user_regist(request):
    if request.method =='POST':
        get_user_id = request.POST.get('user_id')
        get_password = request.POST.get('password')
        if len(get_user_id)==0 and len(get_password)==0:
            return HttpResponse("Wrong")
        exist_user_id = Normal_Person.objects.filter(user_id = get_user_id)
        if not exist_user_id:
            if re.match(r'^[0-9]{8,16}$',get_user_id) and re.match(r'^[0-9A-Za-z~`!@#$%^&*()_+{}|:"?><,./;\'[\]\\=-]{8,16}$',get_password):
                new_user = Normal_Person(user_id = get_user_id,password = get_password)
                new_user.save()
                return HttpResponse("Success")
            else:
                return HttpResponse("Wrong")
        else:
            return HttpResponse("Existed")
    else:
        return HttpResponse("Method Error")
