from cryptography.fernet import Fernet
import base64
from django.conf import settings
import asyncio
import grpc
from concurrent import futures
from grpcs.generated import auth_pb2
from grpcs.generated import auth_pb2_grpc
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.core.exceptions import ObjectDoesNotExist


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


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    async def ValidateToken(self, request, context):
        try:
            # Decode and verify the token using SimpleJWT
            token = AccessToken(request.token)
            user_id = token["user_id"]
            user = await asyncio.to_thread(User.objects.get, id=user_id)
            return auth_pb2.UserResponse(
                is_valid=True,
                user_id=str(user.id),
                username=user.username,
                email=user.email,
            )
        except (ObjectDoesNotExist, KeyError):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

async def serve():
    server = grpc.aio.server()
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())