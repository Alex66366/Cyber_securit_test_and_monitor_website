# Generated by Django 4.2.6 on 2024-03-18 12:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0002_alter_website_owner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Normal_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(16), django.core.validators.RegexValidator('^[0-9]{8,16}$', message='用户名的长度必须为8到16且为数字')])),
                ('password', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(16), django.core.validators.RegexValidator(message='密码必须为8-16长度的英文字符', regex='^[\\w!@#$%^&*()-+=,./;\\\'[]\\<>?:"{}|`~]{8,16}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Super_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10), django.core.validators.RegexValidator('^[\\u4e00-\\u9fa5]+$', message='Field must be Chinese characters.')])),
                ('password', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(16), django.core.validators.RegexValidator(message='密码必须为8-16长度的英文字符', regex='^[\\w!@#$%^&*()-+=,./;\\\'[]\\<>?:"{}|`~]{8,16}$')])),
            ],
        ),
        migrations.AddField(
            model_name='website_owner',
            name='id_card_number',
            field=models.CharField(default='000000000000000000', max_length=18, validators=[django.core.validators.RegexValidator(message='Field must be a valid Chinese ID card number.', regex='^\\d{17}(\\d|X|x)$')]),
        ),
        migrations.AddField(
            model_name='website_owner',
            name='real_name',
            field=models.CharField(default='小明', max_length=20, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20), django.core.validators.RegexValidator('^[\\u4e00-\\u9fa5]+$', message='Field must be Chinese characters.')]),
        ),
        migrations.AlterField(
            model_name='website_owner',
            name='user',
            field=models.CharField(default='00000000', max_length=16, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(16), django.core.validators.RegexValidator('^[a-zA-Z0-9]{8,16}$', message='User must be 8-16 characters long and contain only letters and numbers.')]),
        ),
        migrations.CreateModel(
            name='Owner_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ManyToManyField(related_name='Owner_images', to='regist.image')),
                ('website_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regist.website_owner')),
            ],
        ),
    ]
