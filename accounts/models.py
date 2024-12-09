from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.files.storage import default_storage
import os
from .backends import MainUserManager
from enum import Enum
from .utils import user_profile_directory_path

class UserRoles(Enum):
    BUYER = 'buyer'
    SELLER = 'seller'

class MainUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=10,
        choices=[(role.value, role.name) for role in UserRoles],
        blank=True, null=True
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile_directory_path, blank=True, null=True)
    is_subscribed = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)

    objects = MainUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Check if the user already has a profile picture
        if self.pk:
            old_user = MainUser.objects.filter(pk=self.pk).first()
            if old_user and old_user.profile_picture and old_user.profile_picture != self.profile_picture:
                # Delete the old profile picture file if it exists and is different
                if default_storage.exists(old_user.profile_picture.path):
                    default_storage.delete(old_user.profile_picture.path)

        super().save(*args, **kwargs)