from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('/', BookListCreateView.as_view(), name='book-list-create'),  # GET to list, POST to create
    path('/<str:id>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),  # GET, PUT, PATCH, DELETE
]