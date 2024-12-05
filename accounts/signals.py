import re
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Preprocess username to ensure it's properly formatted
@receiver(pre_save, sender=User)
def preprocess_username(sender, instance, **kwargs):
    if instance.username:
        # Convert to lowercase and replace spaces with dashes
        cleaned_username = instance.username.lower().replace(' ', '-')

        # Remove any non-alphanumeric characters, allowing only letters, numbers, and dashes
        cleaned_username = re.sub(r'[^a-z0-9-]', '', cleaned_username)

        # Ensure username doesn't start with multiple '@' and add a single '@'
        if cleaned_username.startswith('@'):
            cleaned_username = cleaned_username.lstrip('@')
        instance.username = f"@{cleaned_username}" if cleaned_username else "@anonymous"
    else:
        # If username is empty, fall back to the first_name
        cleaned_username = (
            instance.first_name.lower().replace(' ', '-')
            if instance.first_name else "anonymous"
        )
        cleaned_username = re.sub(r'[^a-z0-9-]', '', cleaned_username)
        instance.username = f"@{cleaned_username}"

# Ensure unique email address
@receiver(pre_save, sender=User)
def ensure_unique_email(sender, instance, **kwargs):
    if User.objects.filter(email=instance.email).exclude(pk=instance.pk).exists():
        raise ValidationError("Email address must be unique.")
