# Generated by Django 4.2 on 2023-06-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0005_alter_generatedtask_options_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('1', 'Mathematics'), ('2', 'History'), ('3', 'Science')], max_length=20),
        ),
    ]
