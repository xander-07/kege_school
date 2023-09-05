from django.urls import path
from . import views

urlpatterns = [
    path('', views.inf_home, name='inf_home'),
    path('generate-variant/', views.generate_variant, name='generate_variant'),
    # path('create-generated-task/', views.create_generated_task, name='create_generated_task'),
    path('kim/<str:kim>/', views.generated_task_detail, name='generated_task_detail'),
    # path('kim/<str:kim>/', views.generated_task_detail, name='generated_task_detail'),
    # path('generate-kim/', views.generate_kim, name='generate_kim'),

]