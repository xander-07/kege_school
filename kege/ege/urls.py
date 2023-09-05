from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ege_home, name='ege_home'),
    # path('create', views.create, name='create'),
    # path('variant/<int:pk>', views.Ege_Variant_DerailView.as_view(), name='variant-detail')
    path('variant/<int:variant_selected>', show_category, name='variant-detail')
]
