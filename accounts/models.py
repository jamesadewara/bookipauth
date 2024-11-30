from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .backends import MainUserManager
from .utils import user_profile_directory_path
from enum import Enum

class UserRoles(Enum):
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    SELLER = 'seller'
    GUEST = 'guest'

class MainUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=10,
        choices=[(role.value, role.name) for role in UserRoles],
        default=UserRoles.GUEST.value
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile_directory_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MainUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'role']

    def __str__(self):
        return self.email