from django.contrib import admin
from .models import Profile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'sex', 'city', ]


admin.site.register(Profile, ProfileAdmin)


class ProfileUser(UserAdmin):
    list_display = ['id', 'last_login', 'first_name', 'last_name', 'email', 'date_joined', 'username', 'is_staff',
                    'is_active']


admin.site.unregister(User)
admin.site.register(User, ProfileUser)
