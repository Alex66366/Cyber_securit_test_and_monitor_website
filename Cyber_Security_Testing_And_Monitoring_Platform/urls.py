"""
URL configuration for Cyber_Security_Testing_And_Monitoring_Platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from regist import views
from main_page import views_main
from signin import views_signin

urlpatterns = [
    path('admin/', admin.site.urls),
    #注册界面
    path('register/',views_signin.Reister_page),
    #注册验证
    path('register/check_register/',views.user_regist),
    path('website_score/',views_main.evaluate_security_of_web_site),
    #普通用户登录界面(初始默认界面)
    path('',views_signin.UserLogin_page),
    #超级管理员登录界面
    path('super_user/',views_signin.Super_UserLogin_page),
    #用户密码核查界面
    path('signin/signin_check/',views_signin.check_normal_person),
    #超级管理员账号密码核查
    path('signin/signin_check_super/',views_signin.check_super_person),
    #主功能界面
    path('main_page/',views_signin.Main_page),
]
