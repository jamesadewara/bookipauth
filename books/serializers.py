from rest_framework import serializers
from .models import Book
from accounts.utils import EncryptionHelper

class BookSerializer(serializers.ModelSerializer):
    encrypted_id = serializers.SerializerMethodField()  # This will hold the encrypted ID when sending data

    class Meta:
        model = Book
        fields = ['encrypted_id', 'title', 'author', 'publisher', 'published_date', 'description', 'categories', 'isbn', 'page_count', 'image_links', 'language', 'rating']

    def get_encrypted_id(self, obj):
        """Return the encrypted ID in the serialized response"""
        encryption_helper = EncryptionHelper()
        return encryption_helper.encrypt_id(obj.id)  # Encrypt the ID when sending the API response

    def validate(self, data):
        """Decrypt the ID when receiving it in the API request"""
        if 'encrypted_id' in data:
            encryption_helper = EncryptionHelper()
            decrypted_id = encryption_helper.decrypt_id(data['encrypted_id'])
            data['id'] = decrypted_id  # Decrypt the ID when receiving it in the API request
        return data
