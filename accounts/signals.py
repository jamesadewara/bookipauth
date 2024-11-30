from django.db.models.signals import pre_save
from django.dispatch import receiver
import re

# Preprocess username to ensure it's properly formatted
@receiver(pre_save, sender=User)
def preprocess_username(sender, instance, **kwargs):
    if instance.username:
        # Convert to lowercase and replace spaces with dashes
        cleaned_username = instance.username.lower().replace(' ', '-')
        
        # Remove any non-alphanumeric characters, allowing only letters and numbers
        cleaned_username = re.sub(r'[^a-z0-9-]', '', cleaned_username)
        
        # Ensure there is only one @ at the beginning
        if cleaned_username.startswith('@'):
            cleaned_username = cleaned_username.lstrip('@')
        
        # Prefix with a single @
        instance.username = f"@{cleaned_username}"
       