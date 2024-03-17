from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#创建存放网站持有者的信息的表
class Website_Owner(models.Model):
    real_name = models.CharField(max_length=20, validators=[
        MinLengthValidator(1),
        MaxLengthValidator(20),
        RegexValidator(r'^[\u4e00-\u9fa5]+$', message='Field must be Chinese characters.')
    ])
    id_card_number = models.CharField(max_length=18, validators=[
        RegexValidator(
            regex=r'^\d{17}(\d|X|x)$',
            message='Field must be a valid Chinese ID card number.'
        )
    ])
    user = models.CharField(max_length=16, validators=[
        MinLengthValidator(8),
        MaxLengthValidator(16),
        RegexValidator(r'^[a-zA-Z0-9]{8,16}$',
                       message='User must be 8-16 characters long and contain only letters and numbers.')
    ]) #当输入用户名不满足条件时，会抛出会抛出 ValidationError 异常

    def __str__(self):#用来正常显示用户的用户名
        return str(self.user)
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Owner_Image(models.Model):
    website_owner = models.ForeignKey(Website_Owner, on_delete=models.CASCADE)
    image = models.ManyToManyField(Image, related_name= 'Owner_images')  # 假设有一个存储图片的 ImageField 字段



#创建存放所有用户的信息的表
class Normal_Person(models.Model):
    user_id = models.CharField(max_length= 16,validators=[
        MinLengthValidator(8),
        MaxLengthValidator(16),
        RegexValidator(r'^[0-9]{8,16}$',
                       message= '用户名的长度必须为8到16且为数字')
    ])
    password = models.CharField(max_length=16, validators=[
        MinLengthValidator(8),
        MaxLengthValidator(16),
        RegexValidator(regex=r'^[\w!@#$%^&*()-+=,./;\'[]\<>?:"{}|`~]{8,16}$',
                       message='密码必须为8-16长度的英文字符')
    ])

class Super_Person(models.Model):
    user_id = models.CharField(max_length=10, validators=[
        MinLengthValidator(1),
        MaxLengthValidator(10),
        RegexValidator(r'^[\u4e00-\u9fa5]+$', message='Field must be Chinese characters.')
    ])
    password = models.CharField(max_length=16, validators=[
        MinLengthValidator(8),
        MaxLengthValidator(16),
        RegexValidator(regex=r'^[\w!@#$%^&*()-+=,./;\'[]\<>?:"{}|`~]{8,16}$',
                       message='密码必须为8-16长度的英文字符')
    ])



