# Generated by Django 4.2 on 2023-06-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
    ]