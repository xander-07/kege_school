# Generated by Django 4.2 on 2023-06-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0023_task_level_alter_task_linked_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='task',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
    ]
