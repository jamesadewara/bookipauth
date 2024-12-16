from cryptography.fernet import Fernet
import base64
from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

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

    def encode_urlid(user_id):
        return urlsafe_base64_encode(force_bytes(user_id))

    def decode_urlid(encoded_id):
        return force_str(urlsafe_base64_decode(encoded_id))

def user_profile_directory_path(instance, filename):
    """
    Generates file path to save the user's profile picture.
    The image will be stored as 'profile_pictures/<user_email>.extension'.
    """
    email = instance.email.split('@')[0]  # Get the part before @
    extension = filename.split('.')[-1]  # Get file extension
    return f"profile_pictures/{email}.{extension}"


def send_subscription_email(user_email):
    subject = "Subscription Confirmation"
    message = "Thank you for subscribing to our service!"
    from_email = f"Bookip <noreply@{settings.MAILGUN_DOMAIN}>"
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silentily=False)
        print("Subscription email sent successfully!")
    except Exception as e:
        print("Failed to send subscription email.")
        print(str(e))