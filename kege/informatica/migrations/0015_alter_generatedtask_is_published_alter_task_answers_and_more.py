# Generated by Django 4.2 on 2023-06-03 14:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0014_generatedtask_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedtask',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Открытый доступ'),
        ),
        migrations.AlterField(
            model_name='task',
            name='answers',
            field=models.TextField(verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='questions',
            field=ckeditor.fields.RichTextField(verbose_name='Задание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27')], max_length=20, verbose_name='Тип задания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
