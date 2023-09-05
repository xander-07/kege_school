# Generated by Django 4.2 on 2023-06-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0008_generatedtask_title_alter_generatedtask_kim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedtask',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата составления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generatedtask',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
