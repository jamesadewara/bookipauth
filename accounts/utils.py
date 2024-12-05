import requests
from cryptography.fernet import Fernet
import base64
from django.conf import settings

# Generate a key (run this once and store in your settings securely)
# key = Fernet.generate_key().decode()
# Add this key to your settings: `ENCRYPTION_KEY = 'your-generated-key'`

class EncryptionHelper:
    def __init__(self):
        self.key = settings.ENCRYPTION_KEY.encode()
        self.fernet = Fernet(self.key)

    def encrypt_id(self, user_id):
        """Encrypts the user ID."""
        encrypted_id = self.fernet.encrypt(str(user_id).encode())
        return base64.urlsafe_b64encode(encrypted_id).decode()

    def decrypt_id(self, encrypted_id):
        """Decrypts the encrypted user ID."""
        decoded_encrypted_id = base64.urlsafe_b64decode(encrypted_id.encode())
        decrypted_id = self.fernet.decrypt(decoded_encrypted_id)
        return int(decrypted_id.decode())

def user_profile_directory_path(instance, filename):
    """
    Generates file path to save the user's profile picture.
    The image will be stored as 'profile_pictures/<user_email>.extension'.
    """
    email = instance.email.split('@')[0]  # Get the part before @
    extension = filename.split('.')[-1]  # Get file extension
    return f"profile_pictures/{email}.{extension}"

def send_subscription_email(user_email):
    request_url = f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages"
    
    response = requests.post(
        request_url,
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": f"Bookip <noreply@{settings.MAILGUN_DOMAIN}>",
            "to": [user_email],
            "subject": "Subscription Confirmation",
            "text": "Thank you for subscribing to our service!",
        },
    )
    
    if response.status_code == 200:
        print("Subscription email sent successfully!")
    else:
        print("Failed to send subscription email.")
        print(response.json())
