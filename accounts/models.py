from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.files.storage import default_storage
from django.utils.timezone import now 
from datetime import timedelta
from .backends import MainUserManager
from enum import Enum
from .utils import user_profile_directory_path
import uuid

class UserRoles(Enum):
    BUYER = 'buyer'
    SELLER = 'seller'


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MainUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=[(role.value, role.name) for role in UserRoles],
        blank=True, null=True
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile_directory_path, blank=True, null=True)
    is_subscribed = models.BooleanField(default=False)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    subscription_expiry = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    objects = MainUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def subscribe(self, plan):
        """Subscribe the user to a plan."""
        self.subscription_plan = plan
        self.is_subscribed = True
        self.subscription_expiry = now().date() + timedelta(days=plan.duration_days)
        self.save()

    def cancel_subscription(self):
        """Cancel the subscription."""
        self.subscription_plan = None
        self.is_subscribed = False
        self.subscription_expiry = None
        self.save()

    def save(self, *args, **kwargs):
        # Check if the user already has a profile picture
        if self.pk:
            old_user = MainUser.objects.filter(pk=self.pk).first()
            if old_user and old_user.profile_picture and old_user.profile_picture != self.profile_picture:
                # Delete the old profile picture file if it exists and is different
                old_picture_path = old_user.profile_picture.path if old_user.profile_picture else None
                if old_picture_path and default_storage.exists(old_picture_path):
                    default_storage.delete(old_picture_path)

        super().save(*args, **kwargs)
