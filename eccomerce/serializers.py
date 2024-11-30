from rest_framework import serializers
from .models import (
    Book, BookCategory, Order, Seller, SellerDashboard, Payment,
    Inventory, Review, Shipping, Tax
)
from accounts.utils import EncryptionHelper


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    encrypted_id = serializers.SerializerMethodField()
    categories = BookCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'encrypted_id', 'title', 'author', 'publisher', 'published_date',
            'description', 'categories', 'isbn', 'page_count', 'image_links',
            'price', 'quantity_available', 'language', 'rating'
        ]

    def get_encrypted_id(self, obj):
        encryption_helper = EncryptionHelper()
        return encryption_helper.encrypt_id(obj.id)


class OrderSerializer(serializers.ModelSerializer):
    encrypted_id = serializers.SerializerMethodField()
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'encrypted_id', 'customer', 'books', 'total_price', 'status',
            'shipping_address', 'payment_status', 'order_date'
        ]

    def get_encrypted_id(self, obj):
        encryption_helper = EncryptionHelper()
        return encryption_helper.encrypt_id(obj.id)


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SellerDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerDashboard
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'
