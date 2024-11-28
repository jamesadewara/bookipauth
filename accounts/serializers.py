from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from accounts.models import MainUser

class MainRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=15, required=False)

    def main_signup(self, request, user):
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save()
