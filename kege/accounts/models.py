from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=False)
    email = models.EmailField('Электронная почта', unique=True)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30, blank=True)
    class_number = models.PositiveSmallIntegerField('Класс', null=True, blank=True)
    class_letter = models.CharField('Буква', max_length=1, null=True, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofile', null=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    bio = models.TextField('О себе', max_length=500, blank=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.user.username
