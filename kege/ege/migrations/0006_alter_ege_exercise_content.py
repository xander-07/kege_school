# Generated by Django 4.2 on 2023-05-24 16:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ege', '0005_alter_ege_exercise_additional_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ege_exercise',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=100, null=True, verbose_name='Задание'),
        ),
    ]
