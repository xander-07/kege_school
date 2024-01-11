from django.core.signals import request_finished
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.shortcuts import render, redirect

from .models import Task, GeneratedTask

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from django.contrib import messages

from django.http import JsonResponse
from .models import UserAnswers
from django.db import transaction

from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Value
from django.db.models.functions import Coalesce
from .models import Attempt

# Ручной код
import time
import json
from django.utils import timezone
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from django.http import Http404


@login_required(login_url='')
def inf_home(request):
    user = request.user

    if not user.is_confirmed:
        messages.warning(request,
                         'Ваш email не подтвержден. Пожалуйста, подтвердите его, перейдя по ссылке в письме, которое мы вам отправили.')

    variant = GeneratedTask.objects.filter(is_published=True)
    return render(request, 'inf/inf_home.html', {'variant': variant, 'user': user})


@login_required
def get_one_task_of_each_type(request):
    tasks = []
    task_types = set()
    for task_type in Task.TASK_TYPES:
        if task_type[0] == 1:
            task = Task.objects.filter(task_type=1).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 2:
            task = Task.objects.filter(task_type=2).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 3:
            task = Task.objects.filter(task_type=3).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 4:
            task = Task.objects.filter(task_type=4).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 5:
            task = Task.objects.filter(task_type=5).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 6:
            task = Task.objects.filter(task_type=6).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 7:
            task = Task.objects.filter(task_type=7).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 8:
            task = Task.objects.filter(task_type=8).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 9:
            task = Task.objects.filter(task_type=9).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 10:
            task = Task.objects.filter(task_type=10).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 11:
            task = Task.objects.filter(task_type=11).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 12:
            task = Task.objects.filter(task_type=12).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 13:
            task = Task.objects.filter(task_type=13).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 14:
            task = Task.objects.filter(task_type=14).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 15:
            task = Task.objects.filter(task_type=15).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 16:
            task = Task.objects.filter(task_type=16).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 17:
            task = Task.objects.filter(task_type=17).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 18:
            task = Task.objects.filter(task_type=18).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 19:
            task_19 = Task.objects.filter(task_type=19).order_by('?').first()
            tasks.append(task_19)
            if task_19 is not None:
                linked_tasks_20 = Task.objects.filter(task_type=20, linked_task=task_19.id)
                linked_tasks_21 = Task.objects.filter(task_type=21, linked_task=task_19.id)
                for linked_task in linked_tasks_20:
                    tasks.append(linked_task)
                    task_types.add(linked_task.task_type)
                for linked_task in linked_tasks_21:
                    tasks.append(linked_task)
                    task_types.add(linked_task.task_type)
        if task_type[0] == 20:
            continue
        if task_type[0] == 21:
            continue
        if task_type[0] == 22:
            task = Task.objects.filter(task_type=22).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 23:
            task = Task.objects.filter(task_type=23).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 24:
            task = Task.objects.filter(task_type=24).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 25:
            task = Task.objects.filter(task_type=25).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 26:
            task = Task.objects.filter(task_type=26).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        if task_type[0] == 27:
            task = Task.objects.filter(task_type=27).order_by('?').first()
            tasks.append(task)
            task_types.add(task_type[0])
        # когда ошибка закометь условие тогда
        # else:
        #     task = Task.objects.filter(task_type=task_type[0]).order_by('?').first()
        #     if task is not None:
        #         tasks.append(task)
        #         task_types.add(task_type[0])
        if len(task_types) == len(Task.TASK_TYPES):
            break
    return tasks


@login_required
def generate_variant(request):
    # tasks = Task.objects.all().order_by('?')[:10]  # выбираем 10 случайных заданий
    # tasks = Task.objects.all()
    variant_tasks = get_one_task_of_each_type(request)
    context = {'tasks': variant_tasks}
    html = render_to_string('inf/variant.html', context)
    generated_task = GeneratedTask.objects.create()  # создаем новый вариант в базе данных
    generated_task.tasks.set(variant_tasks)  # связываем задания с вариантом
    generated_task.save()

    Attempt.objects.create(
        id_kim=generated_task.kim,
        user_id=request.user.id,
        finished=False,
        fullname=request.user.get_full_name(),
        time=235 * 60
    )

    # Attempt.objects.create(
    #     id_kim=generated_task.kim,
    #     user_id=request.user,
    #     fullname=request.user.get_full_name(),
    #     time=235  # начальное значение времени
    # )

    # return HttpResponse(html)
    return redirect('generated_task_detail', kim=generated_task.kim)


@login_required
def generated_task_detail(request, kim):
    generated_task = get_object_or_404(GeneratedTask, kim=kim)
    tasks = generated_task.tasks.all()
    user = request.user
    user_id = user.id

    count_answer = UserAnswers.objects.filter(user_id=user_id, kim=kim, finished=0).count()

    task_id = UserAnswers.objects.filter(user_id=user_id, kim=kim, finished=0)
    task_id_list = list(task_id.values_list('id_question', flat=True))

    user_answers = UserAnswers.objects.filter(user_id=user_id, kim=kim, finished=0)
    user_answers_list = list(user_answers.values_list('answer', flat=True))

    answers_user = dict(zip(task_id_list, user_answers_list))

    print(answers_user)

    # for task_s in task_save:
    #     save_id.append(task_s.id_question)
    #
    # save_id.sort()

    def get_answer(task_id):
        return answers_user.get(task_id, '')

    context = {'generated_task': generated_task, 'tasks': tasks, 'count_answer': count_answer,
               'task_save_id': task_id_list, 'user_answers': user_answers_list, 'answers_user': answers_user,
               'get_answer': get_answer}
    return render(request, 'inf/variant.html', context)


def download_file(request, file_id):
    task = get_object_or_404(Task, id=file_id)
    file_path = None

    # Определите, какое поле файла использовать в зависимости от конкретной ситуации.
    # Например, допустим, вы хотите скачать файл_1
    file_field = task.files_1

    if file_field:
        file_path = file_field.path

    if file_path:
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        # Обработка случая, если файл не найден
        return HttpResponse('Файл не найден', status=404)


# Мой код
# @login_required
# def save_answer(request):
#     if request.method == 'POST':
#         data = request.POST
#         user = request.user
#         user_full_name = user.last_name + ' ' + user.first_name + ' ' + user.middle_name
#
#         # Получение остальных данных из POST-запроса
#         answer = data.get('answer_text')
#         id_question = data.get('id_question')
#         kim = data.get('kim')
#         id_kim = data.get('id_kim')
#
#         id_attempt = Attempt.objects.get(user_id=user.id, finished=0, id_kim=id_kim)
#
#         if id_attempt:
#             try:
#                 with transaction.atomic():
#                     # Поиск записи в базе данных
#                     user_answer = UserAnswers.objects.filter(user=user, id_question=id_question, finished=False).first()
#
#                     if user_answer:
#                         # Если запись существует и не завершена, обновляем значения
#                         user_answer.answer = answer
#                         user_answer.save()
#                     else:
#                         # Иначе, создаем новую запись
#                         UserAnswers.objects.create(
#                             user=user,
#                             user_full_name=user_full_name,
#                             answer=answer,
#                             id_question=id_question,
#                             kim=kim,
#                             id_kim=id_kim,
#                             finished=False  # Новая запись, поэтому finished = False
#                         )
#                 return JsonResponse({'status': 'success'})
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': str(e)})
#
#         if Attempt.DoesNotExist:
#             UserAnswers.objects.filter(user_id=user.id, finished=0, id_kim=id_kim).update(finished=1)
#             return JsonResponse({'status': '200', 'message': 'Редактирование запрешено, время вышло'})
#
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@login_required
def save_answer(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        user_full_name = f"{user.last_name} {user.first_name} {user.middle_name}"

        # Получение остальных данных из POST-запроса
        answer = data.get('answer_text')
        id_question = data.get('id_question')
        kim = data.get('kim')
        id_kim = data.get('id_kim')

        type_answer = data.get('type')
        if type_answer == '17' or type_answer == '18' or type_answer == '19' or type_answer == '20' or type_answer == '26' or type_answer == '27':
            answer_get_server = Task.objects.get(id=id_question)
            answer_1 = answer_get_server.answer_1
            additional_1 = answer_get_server.additional_1
            answer = str(answer).split(',')
            if answer[0] == answer_1 and answer[1] == additional_1:
                ball = 1
            else:
                ball = 0

        elif type_answer == '25':
            answer_get_server = Task.objects.get(id=id_question)
            answer_1 = answer_get_server.answer_1
            answer_2 = answer_get_server.answer_2
            answer_3 = answer_get_server.answer_3 or ""
            answer_4 = answer_get_server.answer_4 or ""
            answer_5 = answer_get_server.answer_5 or ""
            answer_6 = answer_get_server.answer_6 or ""
            answer_7 = answer_get_server.answer_7 or ""
            answer_8 = answer_get_server.answer_8 or ""
            answer_9 = answer_get_server.answer_9 or ""
            answer_10 = answer_get_server.answer_10 or ""
            additional_1 = answer_get_server.additional_1
            additional_2 = answer_get_server.additional_2
            additional_3 = answer_get_server.additional_3 or ""
            additional_4 = answer_get_server.additional_4 or ""
            additional_5 = answer_get_server.additional_5 or ""
            additional_6 = answer_get_server.additional_6 or ""
            additional_7 = answer_get_server.additional_7 or ""
            additional_8 = answer_get_server.additional_8 or ""
            additional_9 = answer_get_server.additional_9 or ""
            additional_10 = answer_get_server.additional_10 or ""
            answer = str(answer).split(',')
            if answer[0] == answer_1 and answer[1] == additional_1 and answer[2] == answer_2 and answer[
                3] == additional_2 and answer[4] == answer_3 and answer[5] == additional_3 and answer[6] == answer_4 and \
                    answer[7] == additional_4 and answer[8] == answer_5 and answer[9] == additional_5 and answer[
                10] == answer_6 and answer[11] == additional_6 and answer[12] == answer_7 and answer[
                13] == additional_7 and answer[14] == answer_8 and answer[15] == additional_8 and answer[
                16] == answer_9 and answer[17] == additional_9 and answer[18] == answer_10 and answer[19] == additional_10:
                ball = 1
            else:
                ball = 0
        else:
            answer_get_server = Task.objects.get(id=id_question)
            answer_true = answer_get_server.answer_1
            if answer == answer_true:
                ball = 1
            else:
                ball = 0

        try:
            # Поиск записи в базе данных
            id_attempt = get_object_or_404(Attempt, user_id=user.id, finished=False, id_kim=kim)
            user_answer = UserAnswers.objects.get(user=user, id_question=id_question, finished=False,
                                                  id_attempt=id_attempt.id)

            # Если запись существует и не завершена, обновляем значения
            user_answer.answer = answer
            user_answer.ball = ball
            user_answer.save()

        except UserAnswers.DoesNotExist:
            # Если запись не существует, создаем новую запись
            UserAnswers.objects.create(
                user=user,
                id_question=id_question,
                finished=False,
                user_full_name=user_full_name,
                answer=answer,
                kim=kim,
                id_kim=id_kim,
                id_attempt=id_attempt.id,
                ball=ball
            )

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@csrf_exempt  # Это временное решение для отключения CSRF-защиты
def get_data(request):
    if request.method == 'POST':
        # Получаем данные из тела POST-запроса
        data = json.loads(request.body)
        finish = data.get('finish')
        kim = data.get('kim')
        user = request.user
        user_id = user.id
        user_full_name = user.last_name + ' ' + user.first_name + ' ' + user.middle_name
        user_attempt = Attempt.objects.filter(id_kim=kim, user_id=user_id, finished=False).first()

        # Получение времени сервера
        server_time = timezone.now()
        # Форматирование времени в формат час минута секунда
        server_time = server_time.strftime('%H:%M:%S, %d.%m.%Y')

        # time_variant = 235

        if not user_attempt:
            # server_time = server_time + timedelta(hours=3, minutes=55)
            time_variant = GeneratedTask.objects.get(kim=kim).time * 60
            Attempt.objects.create(
                id_kim=kim,
                user_id=user_id,
                finished=False,
                fullname=user_full_name,
                time=time_variant
            )

            response_data = {'status': 200,
                             'message': 'OK',
                             'kim': kim,
                             'user': user_full_name,
                             'time_variant': time_variant,
                             }

        if user_attempt:
            attempt = Attempt.objects.get(user_id=user_id, id_kim=kim, finished=False)
            get_time = attempt.time
            if get_time <= 0 or finish:
                attempt.finished = True
                attempt.save()

                UserAnswers.objects.filter(user_id=user_id, kim=kim, finished=0).update(finished=1)

                response_data = {'status': 200,
                                 'message': 'OK',
                                 'kim': kim,
                                 'user': user_full_name,
                                 'time_variant': get_time,
                                 'finish': 'yes'
                                 }

            else:
                get_time = get_time - 10
                attempt.time = get_time
                attempt.save()

                response_data = {'status': 200,
                                 'message': 'OK',
                                 'kim': kim,
                                 'user': user_full_name,
                                 'time_variant': get_time,
                                 'finish': 'no'
                                 }

        # Здесь вы можете использовать данные и отправить ответ
        # response_data = {'status': 200,
        #                  'message': 'OK',
        #                  'kim': kim,
        #                  'user': user_full_name,
        #                  'time_variant': time_variant,
        #                  }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
