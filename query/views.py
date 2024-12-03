from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from eccomerce.models import Book
from eccomerce.serializers import BookSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class BookSearchView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        genre = request.query_params.get('genre', None)
        language = request.query_params.get('language', None)
        price_min = request.query_params.get('price_min', None)
        price_max = request.query_params.get('price_max', None)
        sort_by = request.query_params.get('sort', 'rating')
        page = int(request.query_params.get('page', 1))

        # Initialize the queryset
        books = Book.objects.all()

        # Full-text search
        if query:
            search_query = SearchQuery(query)
            books = books.annotate(
                search=SearchVector('title', 'author', 'description'),
                rank=SearchRank('search', search_query)
            ).filter(search=search_query).order_by('-rank')

        # Apply filters
        if genre:
            books = books.filter(genre__icontains=genre)
        if language:
            books = books.filter(language__icontains=language)
        if price_min:
            books = books.filter(price__gte=price_min)
        if price_max:
            books = books.filter(price__lte=price_max)

        # Sorting
        if sort_by == 'price':
            books = books.order_by('price')
        elif sort_by == 'popularity':
            books = books.order_by('-rating')
        else:
            books = books.order_by('-rating')  # Default to sorting by rating

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # You can set your own page size
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)