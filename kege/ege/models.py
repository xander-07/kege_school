from django.db import models
from ckeditor.fields import RichTextField

# class Article(models.Model):
#     title=models.CharField('Title', max_length=200)
#     text=CKEditor5Field('Text', config_name='extends')

LEVEL = (
    ('H', 'Сложный'),
    ('M', 'Средний'),
    ('L', 'Базовый')
)

NUMBER = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27')
)


class Ege_Variants(models.Model):
    title = models.CharField('Название варианта', max_length=50)
    kim = models.CharField('КИМ', max_length=8, db_index=True)
    description = models.TextField('Описание варианта', max_length=250, null=True)
    level = models.CharField('Уровень', max_length=50, null=True, choices=LEVEL)
    time_create = models.DateTimeField('Дата составления', auto_now_add=True)
    time_update = models.DateTimeField('Дата обновления', auto_now=True)
    is_published = models.BooleanField('Открытый доступ', default=True)

    # def get_absolute_url(self):
    #     return reversed('variant', kwargs={'variant_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Ege_Exercise(models.Model):
    kim = models.ForeignKey('Ege_Variants', on_delete=models.PROTECT, null=True, blank=True)
    level = models.CharField('Уровень сложности', max_length=50, choices=LEVEL)
    title = models.CharField('Название задания', max_length=50, null=True)
    type = models.CharField('Тип задания (1-27)', max_length=100, null=True, choices=NUMBER)
    content = RichTextField('Задание')
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
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    time_update = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
