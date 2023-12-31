# Generated by Django 4.2 on 2023-06-06 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_patronymic'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('class_name', models.IntegerField(blank=True, null=True)),
                ('class_letter', models.CharField(blank=True, max_length=1, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('class_name', models.IntegerField(blank=True, null=True)),
                ('class_letter', models.CharField(blank=True, max_length=1, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
