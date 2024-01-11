from django.db import models
from ckeditor.fields import RichTextField
import random
from django.core.exceptions import ValidationError
from accounts.models import CustomUser


class Task(models.Model):
    LEVEL = (
        ('H', 'Сложный'),
        ('M', 'Средний'),
        ('L', 'Базовый')
    )

    TASK_TYPES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
    )
    task_type = models.IntegerField(choices=TASK_TYPES, verbose_name='Тип задания')
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    description = models.CharField(verbose_name='Описание', max_length=255)
    questions = RichTextField('Задание')
    linked_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='К заданию (прикрепить)')
    level = models.CharField('Уровень сложности', max_length=50, choices=LEVEL, null=True)
    # answers = models.CharField(verbose_name='Ответ')
    answer_1 = models.CharField('Ответ на задание (основной)', max_length=120, null=True)
    additional_1 = models.CharField('Ответ на задание (основной_доп)', max_length=120, null=True, blank=True)
    answer_2 = models.CharField('Ответ на задание (2)', max_length=120, null=True, blank=True)
    additional_2 = models.CharField('Ответ на задание (доп_2)', max_length=120, null=True, blank=True)
    answer_3 = models.CharField('Ответ на задание (3)', max_length=120, null=True, blank=True)
    additional_3 = models.CharField('Ответ на задание (доп_3)', max_length=120, null=True, blank=True)
    answer_4 = models.CharField('Ответ на задание (4)', max_length=120, null=True, blank=True)
    additional_4 = models.CharField('Ответ на задание (доп_4)', max_length=120, null=True, blank=True)
    answer_5 = models.CharField('Ответ на задание (5)', max_length=120, null=True, blank=True)
    additional_5 = models.CharField('Ответ на задание (доп_5)', max_length=120, null=True, blank=True)
    answer_6 = models.CharField('Ответ на задание (6)', max_length=120, null=True, blank=True)
    additional_6 = models.CharField('Ответ на задание (доп_6)', max_length=120, null=True, blank=True)
    answer_7 = models.CharField('Ответ на задание (7)', max_length=120, null=True, blank=True)
    additional_7 = models.CharField('Ответ на задание (доп_7)', max_length=120, null=True, blank=True)
    answer_8 = models.CharField('Ответ на задание (8)', max_length=120, null=True, blank=True)
    additional_8 = models.CharField('Ответ на задание (доп_8)', max_length=120, null=True, blank=True)
    answer_9 = models.CharField('Ответ на задание (9)', max_length=120, null=True, blank=True)
    additional_9 = models.CharField('Ответ на задание (доп_9)', max_length=120, null=True, blank=True)
    answer_10 = models.CharField('Ответ на задание (10)', max_length=120, null=True, blank=True)
    additional_10 = models.CharField('Ответ на задание (доп_10)', max_length=120, null=True, blank=True)
    files_1 = models.FileField('Файл_1', null=True, blank=True)
    files_2 = models.FileField('Файл_2', null=True, blank=True)
    files_3 = models.FileField('Файл_3', null=True, blank=True)
    files_4 = models.FileField('Файл_4', null=True, blank=True)
    files_5 = models.FileField('Файл_5', null=True, blank=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    time_update = models.DateTimeField('Дата обновления', auto_now=True, null=True)

    def clean(self):
        if self.task_type in [20, 21] and self.linked_task is None:
            raise ValidationError('Для типов 20 и 21 необходимо указать задание, на которое они ссылается.')
        if self.task_type == 19 and self.linked_task is not None:
            raise ValidationError('Для типа 19 ссылка на другое задание не допускается.')
        if self.task_type == 20 and self.linked_task.task_type != 19:
            raise ValidationError('Для типа 20 ссылка на задание допустима только для типа 19.')
        if self.task_type == 21 and self.linked_task.task_type != 19:
            raise ValidationError('Для типа 21 ссылка на задание допустима только для типа 19.')

    # number = models.PositiveIntegerField(unique=True, null=True)

    # def save(self, *args, **kwargs):
    #     if not self.number:
    #         last_task = Task.objects.order_by('-number').first()
    #         self.number = last_task.number + 1 if last_task else 1
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'

    def __str__(self):
        return f'{self.pk}'


class GeneratedTask(models.Model):
    kim = models.CharField(max_length=8, unique=True, verbose_name='КИМ')
    tasks = models.ManyToManyField(Task, verbose_name='Задания')
    is_published = models.BooleanField('Открытый доступ', default=False)
    title = models.CharField(max_length=255, verbose_name="Отображаемое название", null=True, blank=True)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    time_update = models.DateTimeField('Дата обновления', auto_now=True, null=True)
    time = models.IntegerField('Время на выполнение варианта в минутах',null=True, blank=True, default=235)
    files_1 = models.FileField('Картинка', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.kim:
            self.kim = generate_kim()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'вариант'
        verbose_name_plural = 'варианты'

    def __str__(self):
        return f'КИМ №{self.kim}'

    # def __str__(self):
    #     return self.kim


def generate_kim():
    return str(random.randint(10000000, 99999999))


class UserAnswers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    user_full_name = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    id_question = models.IntegerField(null=True, blank=True)
    id_kim = models.IntegerField(null=True, blank=True)
    kim = models.CharField(max_length=255, null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField(null=True, blank=True)
    finished = models.BooleanField(default=False, null=True, blank=True)
    id_attempt = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'ответ пользователя'
        verbose_name_plural = 'ответы пользователей'


class Attempt(models.Model):
    id_kim = models.IntegerField()
    time = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)
