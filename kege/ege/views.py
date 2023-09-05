from django.shortcuts import render, redirect, HttpResponse
from .models import Ege_Variants, Ege_Exercise
from django.views.generic import DetailView

def ege_home(request):
    variant = Ege_Variants.objects.filter(is_published=True)
    tasks = Ege_Exercise.objects.filter()
    return render(request, 'ege/ege_home.html', {'variant': variant, 'tasks': tasks})


# class Ege_Variant_DerailView(DetailView):
#     model = Ege_Variants
#     # variant = Ege_Exercise.objects.filter(variant=variant)
#     template_name = 'ege/ege_details_view.html'
#     context_object_name = 'variant'


def show_category(request, variant_selected):
    tasks = Ege_Exercise.objects.filter(kim=variant_selected)
    variant = Ege_Variants.objects.filter(id=variant_selected)

    # if len(posts) == 0:
    #     raise Http404()

    # context = {
    #     'tasks': tasks,
    #     'variant': variant,
    #     # 'menu': menu,
    #     'title': 'Отображение по рубрикам',
    #     'variant_selected': variant_selected,
    # }

    return render(request, 'ege/kim.html', {'variant': variant, 'tasks': tasks})

# def show_variant(request, variant_id):
#     return HttpResponse(f'Отображение варианта с id = {variant_id}')

# def ege_home(request):
#     return render(request, 'ege/ege_home.html')

# Генрация произвольного варианта


