# Generated by Django 3.2 on 2021-05-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('0', '女')], default='1', max_length=1, verbose_name='性别')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='年龄')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
        ),
    ]
