from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from accounts.models import MainUser

class MainRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=15, required=False)

    def main_signup(self, request, user):
        user.phone_number = self.validated_data.get('phone_number', '')
        user.save()

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['is_subscribed']  # Only expose the subscription field
        read_only_fields = ['email', 'username', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        instance.is_subscribed = validated_data.get('is_subscribed', instance.is_subscribed)
        instance.save()
        return instance
