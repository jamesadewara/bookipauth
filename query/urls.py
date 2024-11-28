from django.urls import path
from .views import BookSearchView

urlpatterns = [
    path('/', BookSearchView.as_view(), name='book_search'),
]
