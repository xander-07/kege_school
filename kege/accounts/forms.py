from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.db.models import Q
from django.forms import ModelForm
from .models import CustomUser, UserProfile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'middle_name', 'class_number', 'class_letter',
                  'birthday']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')

        if username and password:
            user = CustomUser.objects.filter(Q(username=username) | Q(email=username)).first()
            if user:
                raise forms.ValidationError(
                    'Пользователь с таким именем пользователя или электронной почтой уже существует')
        return self.cleaned_data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'middle_name', 'class_number', 'class_letter', 'birthday')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'bio', 'birth_date')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя / Email', max_length=254)

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                'Этот аккаунт заблокирован.',
                code='inactive',
            )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        profile_form = None

        if username and password:
            user = CustomUser.objects.filter(Q(username=username) | Q(email=username)).first()
            if user:
                if not user.check_password(password):
                    raise forms.ValidationError('Неверный пароль')
            else:
                raise forms.ValidationError('Пользователь с таким именем пользователя или электронной почтой не найден')

        return cleaned_data


class CustomUserUpdateForm(ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class_number = forms.ChoiceField(label='Номер класса', choices=[(str(i), str(i)) for i in range(5, 12)],
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    class_letter = forms.CharField(label='Буква класса', max_length=1,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '1'}))
    birthday = forms.DateField(label='Дата рождения',
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.birthday:
            self.fields['birthday'].widget.attrs['value'] = self.instance.birthday.strftime('%Y-%m-%d')

    def clean_class_letter(self):
        class_letter = self.cleaned_data['class_letter']
        return class_letter.upper()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'class_number', 'class_letter', 'birthday']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get('new_password1')

        try:
            validate_password(new_password1, self.user)
        except ValidationError as error:
            raise forms.ValidationError(error)

        return new_password1
