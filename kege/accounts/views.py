from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.tokens import default_token_generator


import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from django.http import Http404

from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileForm, CustomAuthenticationForm, \
    CustomUserUpdateForm, CustomPasswordChangeForm
from .models import CustomUser, UserProfile


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'


class ConfirmRegistrationView(View):
    def get(self, request, token):
        try:
            user = CustomUser.objects.get(token=token, is_confirmed=False)
            user.is_confirmed = True
            user.save()

            # messages.success(request, 'E-mail успешно подтвержден. Теперь вы можете войти.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Неверный токен подтверждения или пользователь уже подтвержден.')

        return redirect('home')


class RegisterView(SuccessMessageMixin, CreateView):
    model = CustomUser
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')  # Заменить 'register' URL для страницы регистрации
    success_message = 'Account created successfully. Please check your email for further instructions.'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Генерация URL для подтверждения регистрации
        token = uuid.uuid4()
        confirmation_url = reverse('confirm_registration', args=[str(token)])

        # Установка токена и статуса подтверждения
        self.object.token = token
        self.object.is_confirmed = False  # Установим статус подтверждения в False при регистрации
        self.object.save()

        # Отправляем письмо с информацией о регистрации и ссылкой на подтверждение
        subject = 'Регистрация на сайте'
        message = (
            f'Добро пожаловать, {self.object.first_name} {self.object.last_name}!\n\n'
            f'Ваши учетные данные:\n'
            f'Логин: {self.object.username}\n'
            f'Пароль: {form.cleaned_data["password1"]}\n\n'
            f'Для подтверждения регистрации перейдите по ссылке: {self.request.build_absolute_uri(confirmation_url)}'
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = self.object.email
        send_mail(subject, message, from_email, [to_email])

        return response

    # def get_success_url(self):
    #     return self.success_url


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=user)
        form_pass = CustomPasswordChangeForm(request.user, request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
        if form_pass.is_valid():
            user = form_pass.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('profile')
    else:
        user_form = CustomUserUpdateForm(instance=user)
        form_pass = CustomPasswordChangeForm(request.user)

    context = {
        'user_form': user_form,
        'user': user,
        'pass': form_pass,
    }

    return render(request, 'accounts/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Этот аккаунт заблокирован.')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = CustomAuthenticationForm(request=request)

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, f'Ваш аккаунт успешно удален')
        return redirect('login')
    return render(request, 'accounts/delete_account.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form_pass = CustomPasswordChangeForm(request.user, request.POST)
        if form_pass.is_valid():
            user = form_pass.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('profile')
    else:
        form_pass = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/profile.html', {'form': form_pass})


@login_required
def change_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            messages.error(request, 'Пользователь с таким email уже существует')
        else:
            request.user.email = email
            request.user.save()
            messages.success(request, f'Ваш email успешно изменен на {email}')
            return redirect('profile')
    return render(request, 'accounts/change_email.html')
