# Generated by Django 4.0.5 on 2022-06-27 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogTypes',
            new_name='BlogType',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_types',
            new_name='blog_type',
        ),
    ]