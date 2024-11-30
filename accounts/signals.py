from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import re

# Preprocess username to ensure it's properly formatted
@receiver(pre_save, sender=User)
def preprocess_username(sender, instance, **kwargs):
    if instance.first_name:  # Check if first_name exists
        # Convert to lowercase and replace spaces with dashes
        cleaned_username = instance.first_name.lower().replace(' ', '-')

        # Remove any non-alphanumeric characters, allowing only letters, numbers, and dashes
        cleaned_username = re.sub(r'[^a-z0-9-]', '', cleaned_username)
    else:
        cleaned_username = "anonymous"

    # Prefix with a single @ and assign it to the username field
    instance.username = f"@{cleaned_username}"
