from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'published_date', 'rating')
    search_fields = ('title', 'author', 'publisher')

admin.site.register(Book, BookAdmin)
