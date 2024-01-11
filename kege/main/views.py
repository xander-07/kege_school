from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


@login_required
def kege(request):
    return render(request, 'main/kege.html')
