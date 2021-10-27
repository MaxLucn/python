# Generated by Django 3.1.7 on 2021-10-27 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='描述')),
                ('types', models.SmallIntegerField(default=10, verbose_name='展现的位置')),
                ('img', models.ImageField(max_length=255, upload_to='%Y%m/slider', verbose_name='图片地址')),
                ('reorder', models.SmallIntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序字段')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='生效开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='生效结束的时间')),
                ('target_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='跳转的地址')),
            ],
            options={
                'db_table': 'system_slider',
                'ordering': ['-reorder'],
            },
        ),
        migrations.CreateModel(
            name='ImageRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('img', models.ImageField(max_length=256, upload_to='%Y%m/file/', verbose_name='图片')),
                ('summary', models.CharField(blank=True, max_length=32, null=True, verbose_name='图片说明')),
                ('object_id', models.IntegerField(verbose_name='关联的模型')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(null=True, on_delete=models.SET(None), related_name='upload_images', to=settings.AUTH_USER_MODEL, verbose_name='上传的用户')),
            ],
            options={
                'db_table': 'system_image_related',
            },
        ),
    ]
