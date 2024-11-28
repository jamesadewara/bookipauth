from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MainUser

class MainUserAdmin(UserAdmin):
    model = MainUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'profile_picture')}),
    )

admin.site.register(MainUser, MainUserAdmin)
