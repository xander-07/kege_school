# Generated by Django 4.2 on 2023-06-02 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0004_remove_task_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generatedtask',
            options={'verbose_name': 'вариант', 'verbose_name_plural': 'варианты'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'задание', 'verbose_name_plural': 'задания'},
        ),
    ]
