from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from .models import CustomUser, UserProfile


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('get_full_name', 'username', 'email', 'is_active', 'is_staff', 'last_login')
    ordering = ('email',)
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff')
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'middle_name', 'class_number', 'class_letter', 'birthday', 'password', 'last_login')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = _('Full Name')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('last_login',)
        return self.readonly_fields


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birth_date')
    search_fields = ('user__email',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        (_('Additional info'), {'fields': ('bio', 'birth_date')}),
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)