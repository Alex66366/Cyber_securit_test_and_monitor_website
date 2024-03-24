from django.contrib import admin
from .models import Website_Owner
from .models import Normal_Person
from .models import Super_Person
# Register your models here.

#在这里注册好，使得我们自己设计的表能在django后台管理页面中显示
admin.site.register(Website_Owner) #注册表
admin.site.register(Normal_Person)
admin.site.register(Super_Person)

