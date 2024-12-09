from rest_framework import serializers
from accounts.models import MainUser

class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name', 
            'role', 'phone_number', 'date_of_birth', 'profile_picture'
        ]
        read_only_fields = ['email', 'role']

class UpdateMainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = [
            'username', 'first_name', 'last_name', 
            'phone_number', 'date_of_birth', 'profile_picture'
        ]

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['is_subscribed']  # Only expose the subscription field
        read_only_fields = ['email', 'username', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        # Update subscription status
        instance.is_subscribed = validated_data.get('is_subscribed', instance.is_subscribed)
        instance.save()
        return instance
