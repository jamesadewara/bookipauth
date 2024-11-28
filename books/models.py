from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Book(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    description = models.TextField()
    categories = models.JSONField()
    isbn = models.CharField(max_length=20)
    page_count = models.IntegerField()
    image_links = models.JSONField()
    language = models.CharField(max_length=50)
    rating = models.FloatField(null=True, blank=True)

    search_vector = SearchVectorField(null=True)  # Full-text search vector field

    def save(self, *args, **kwargs):
        # Automatically update the search vector when saving
        from django.contrib.postgres.search import SearchVector
        self.search_vector = (
            SearchVector('title') + SearchVector('author') + SearchVector('description')
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
