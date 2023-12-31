# Generated by Django 4.2 on 2023-06-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0015_alter_generatedtask_is_published_alter_task_answers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='answers',
        ),
        migrations.AddField(
            model_name='task',
            name='additional_1',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (основной_доп)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_10',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_10)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_2',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_2)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_3',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_3)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_4',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_4)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_5',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_5)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_6',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_6)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_7',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_7)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_8',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_8)'),
        ),
        migrations.AddField(
            model_name='task',
            name='additional_9',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (доп_9)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_1',
            field=models.CharField(max_length=120, null=True, verbose_name='Ответ на задание (основной)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_10',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (10)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_2',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (2)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_3',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (3)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_4',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (4)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_5',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (5)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_6',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (6)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_7',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (7)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_8',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (8)'),
        ),
        migrations.AddField(
            model_name='task',
            name='answer_9',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ответ на задание (9)'),
        ),
        migrations.AddField(
            model_name='task',
            name='files_1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл_1'),
        ),
        migrations.AddField(
            model_name='task',
            name='files_2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл_2'),
        ),
        migrations.AddField(
            model_name='task',
            name='files_3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл_3'),
        ),
        migrations.AddField(
            model_name='task',
            name='files_4',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл_4'),
        ),
        migrations.AddField(
            model_name='task',
            name='files_5',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл_5'),
        ),
    ]
