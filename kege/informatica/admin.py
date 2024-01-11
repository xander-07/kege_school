from django.contrib import admin
from .models import Task, GeneratedTask, UserAnswers

class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(GeneratedTask)
class GeneratedTaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('tasks',)
    search_fields = ['kim']
    list_display = ('id', 'kim', 'is_published', 'Tasks', 'time_create', 'time_update', 'time')

    readonly_fields = ['kim', 'time_create', 'time_update']
    fieldsets = (
        (None, {
            'fields': ('tasks', 'is_published', 'title', 'time')
        }),
        ('Дополнительно', {
            'fields': ('kim', 'time_create', 'time_update', 'files_1'),
            'classes': ('collapse', 'collapse', 'collapse', 'collapse')
        }),
    )

    help_texts = {
        'search_fields': 'Поиск по КИМ'
    }

    def Tasks(self, obj):
        return ', '.join(str(task.task_type) for task in obj.tasks.all())
        # если что вот строка
        # return ', '.join(str(task.task_type) for task in obj.tasks.all() if task.title is not None)

    Tasks.short_description = 'Задания'

    def generate_kim_number(self, request, obj):
        obj.kim_number = GeneratedTask.objects.all().count() + 1
        obj.save()

    generate_kim_number.short_description = 'Сгенерировать номер КИМ'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_type', 'questions', 'answers_1', 'time_create', 'time_update')
    list_select_related = ('linked_task',)

    class Media:
        js = ('inf/js/task_admin.js',)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is not None and obj.task_type not in [20, 21]:
            fields.remove('linked_task')
        return fields

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'linked_task':
            kwargs['queryset'] = Task.objects.filter(task_type=19)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    readonly_fields = ['time_create', 'time_update']

    fieldsets = [
        (None, {'fields': ['task_type', 'linked_task', 'level', 'questions', 'answer_1', 'additional_1']}),
        ('Ответы', {
            'fields': ('answer_2', 'additional_2', 'answer_3', 'additional_3', 'answer_4', 'additional_4', 'answer_5', 'additional_5', 'answer_6', 'additional_6', 'answer_7', 'additional_7', 'answer_8', 'additional_8', 'answer_9', 'additional_9', 'answer_10', 'additional_10'),
            'classes': ('collapse',)
        }),
        ('Файлы', {
            'fields': ('files_1', 'files_2', 'files_3', 'files_4', 'files_5'),
            'classes': ('collapse',)
        }),
        ('Дополнительно', {
            'fields': ('title', 'time_create', 'time_update'),
            'classes': ('collapse',)
        }),
    ]

    def answers_1(self, obj):
        return obj.answer_1

    answers_1.short_description = 'Ответ 1'

admin.site.register(Task, TaskAdmin)
# admin.site.register(GeneratedTask)

# admin.site.register(Task, TaskAdmin)  # удалите эту строку
# admin.site.register(GeneratedTask, GeneratedTaskAdmin)  # удалите эту строку


@admin.register(UserAnswers)
class UserAnswersAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'user_full_name', 'answer', 'id_kim', 'kim', 'time', 'ball')
    search_fields = ['user__username', 'user_full_name', 'kim']



