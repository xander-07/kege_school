# Generated by Django 4.2 on 2023-06-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0007_generatedtask_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedtask',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отображаемое название'),
        ),
        migrations.AlterField(
            model_name='generatedtask',
            name='kim',
            field=models.CharField(max_length=8, unique=True, verbose_name='КИМ'),
        ),
        migrations.AlterField(
            model_name='generatedtask',
            name='tasks',
            field=models.ManyToManyField(to='informatica.task', verbose_name='Задания'),
        ),
    ]
