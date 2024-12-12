from rest_framework import serializers
from accounts.models import MainUser, SubscriptionPlan

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

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'price', 'duration_days', 'description']

class SubscriptionSerializer(serializers.ModelSerializer):
    plan_id = serializers.IntegerField(write_only=True, required=False)
    subscribe = serializers.BooleanField(write_only=True, required=True)

    class Meta:
        model = MainUser
        fields = ['is_subscribed', 'subscription_expiry', 'plan_id', 'subscribe']