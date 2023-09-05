from django.urls import path
from .views import RegisterView, CustomLoginView, logout_view, profile

# app_name = 'accounts'

urlpatterns = [
    # path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]
