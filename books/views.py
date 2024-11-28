from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# View to list all books and create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# View to retrieve, update, or delete a book by id
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'encrypted_id'  # Lookup by 'id' (string field)
