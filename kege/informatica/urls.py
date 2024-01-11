from django.urls import path
from . import views
from .views import download_file, get_data

urlpatterns = [
    path('', views.inf_home, name='inf_home'),
    path('generate-variant/', views.generate_variant, name='generate_variant'),
    path('kim/<str:kim>/', views.generated_task_detail, name='generated_task_detail'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('save-answer/', views.save_answer, name='save_answer'),
    path('get_data/', get_data, name='get_data'),
]
