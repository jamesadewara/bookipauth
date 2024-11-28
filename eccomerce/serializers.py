from rest_framework import serializers
from .models import Order
from ..accounts.utils import EncryptionHelper

class OrderSerializer(serializers.ModelSerializer):
    # Encrypt order_id before returning it in the response
    order_id = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_order_id(self, obj):
        """Encrypt order_id before sending it in response."""
        encryption_helper = EncryptionHelper()
        return encryption_helper.encrypt_id(obj.order_id)

    def to_internal_value(self, data):
        """Decrypt the order_id when receiving data in the request."""
        encryption_helper = EncryptionHelper()
        if 'order_id' in data:
            data['order_id'] = encryption_helper.decrypt_id(data['order_id'])
        return super().to_internal_value(data)
