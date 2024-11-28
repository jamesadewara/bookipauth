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
    """Save files under a directory based on the encrypted user ID."""
    encryption_helper = EncryptionHelper()
    encrypted_id = encryption_helper.encrypt_id(instance.id)
    return f'imgs/profile/{encrypted_id}/{filename}'