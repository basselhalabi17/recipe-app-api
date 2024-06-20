from django.contrib import admin # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # noqa
from django.utils.translation import gettext as _  # noqa
from .models import User  # noqa


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        ('Personal Info', {'fields': ('email',)}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser'),
            },
            ),
        (
            _('Important dates'),
            {
                'fields': ('last_login',),
            },
            ),
    )
    readonly_fields = ('last_login',)
    add_fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }),
    )


admin.site.register(User, UserAdmin)
