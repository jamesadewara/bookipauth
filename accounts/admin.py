from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from .models import MainUser

class MainUserCreationForm(forms.ModelForm):
    """A form for creating new users with email and password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = MainUser
        fields = ('email', 'username', 'first_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MainUserAdmin(BaseUserAdmin):
    """Custom admin interface for MainUser model."""
    add_form = MainUserCreationForm
    list_display = ('email', 'username', 'first_name', 'role', 'is_superuser')
    list_filter = ('role', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role', {'fields': ('role',)}),
        ('Subscription', {'fields': ('is_subscribed',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'role', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'username', 'role')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_fieldsets(self, request, obj=None):
        """Customize the fieldsets based on user privileges."""
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            # Restrict permissions fields for non-superusers
            fieldsets = [
                (name, {'fields': [field for field in opts['fields'] if field not in ('is_superuser', 'groups', 'user_permissions')]})
                for name, opts in fieldsets
            ]
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        """Set certain fields as read-only based on user privileges."""
        if not request.user.is_superuser:
            return ('is_superuser', 'role', 'groups', 'user_permissions')
        return super().get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj=None):
        """Restrict delete permissions for staff users."""
        if not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        """Restrict change permissions for certain fields."""
        if obj and not request.user.is_superuser:
            # Staff cannot change the superuser status or role
            restricted_fields = ('is_superuser', 'role')
            for field in restricted_fields:
                if request.POST.get(field) and getattr(obj, field) != request.POST[field]:
                    return False
        return super().has_change_permission(request, obj)


# Register the custom admin class
admin.site.register(MainUser, MainUserAdmin)