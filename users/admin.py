from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUser, CustomUserChangeForm
    model = UserAdmin
    # list_display = ['username', 'fio', 'gender', 'birth_date', 'email', 'groups']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'groups'
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
