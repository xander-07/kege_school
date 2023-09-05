from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Task, GeneratedTask
import random
from django.shortcuts import render, redirect
from .forms import GeneratedTaskForm
from .models import Task, GeneratedTask
# from .utils import generate_kim, generate_variant_tasks
from random import sample


def inf_home(request):
    variant = GeneratedTask.objects.filter(is_published=True)
    # tasks = Ege_Exercise.objects.filter()
    # return render(request, 'inf/inf_home.html', {'variant': variant, 'tasks': tasks})
    return render(request, 'inf/inf_home.html', {'variant': variant})

# def get_one_task_of_each_type():
#     tasks = []
#     for task_type in Task.TASK_TYPES:
#         task = Task.objects.filter(task_type=task_type[0]).order_by('?').first()
#         if task is not None:
#             tasks.append(task)
#     return tasks


def get_one_task_of_each_type():
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


def generate_variant(request):
    # tasks = Task.objects.all().order_by('?')[:10]  # выбираем 10 случайных заданий
    # tasks = Task.objects.all()
    variant_tasks = get_one_task_of_each_type()
    context = {'tasks': variant_tasks}
    html = render_to_string('inf/variant.html', context)
    generated_task = GeneratedTask.objects.create()  # создаем новый вариант в базе данных
    generated_task.tasks.set(variant_tasks)  # связываем задания с вариантом
    generated_task.save()
    # return HttpResponse(html)
    return redirect('generated_task_detail', kim=generated_task.kim)

# def create_generated_task(request):
#     if request.method == 'POST':
#         form = GeneratedTaskForm(request.POST)
#         if form.is_valid():
#             # tasks = form.cleaned_data['tasks']
#             tasks = Task.objects.all()
#             # context = {'tasks': tasks}
#             context = generate_variant_tasks(tasks)
#             html = render_to_string('inf/variant.html', {'tasks': context})
#             generated_task = GeneratedTask.objects.create()  # создаем новый вариант в базе данных
#             generated_task.tasks.set(tasks)  # связываем задания с вариантом
#             generated_task.save()
#             return redirect('generated_task_detail', kim=generated_task.kim)
#     else:
#         form = GeneratedTaskForm()
#     context = {'form': form}
#     return render(request, 'inf/create_generated_task.html', context)

def generated_task_detail(request, kim):
    generated_task = GeneratedTask.objects.get(kim=kim)
    tasks = generated_task.tasks.all()
    context = {'generated_task': generated_task, 'tasks': tasks}
    return render(request, 'inf/variant.html', context)


# def generate_variant_tasks(tasks):
#     # Создаем список заданий, содержащий по одному заданию каждого типа
#     variant_tasks = []
#     for task_type in Task.TASK_TYPES:
#         task = tasks.filter(task_type=task_type[0]).order_by('?').first()
#         if task is not None:
#             variant_tasks.append(task)
#
#     # Добавляем оставшиеся задания случайного типа
#     remaining_tasks = tasks.exclude(task_type__in=[t.task_type for t in variant_tasks])
#     variant_tasks += list(remaining_tasks.order_by('?')[:3])
#
#     # Возвращаем перемешанный список заданий
#     return sample(variant_tasks, len(variant_tasks))



# def generate_kim(request):
#     tasks = Task.objects.all()
#     variant_tasks = generate_variant_tasks(tasks)
#     return render(request, 'inf/kim.html', {'tasks': variant_tasks})



