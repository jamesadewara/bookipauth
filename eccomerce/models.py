from django.db import models
from decimal import Decimal
from enum import Enum
from django.contrib.postgres.search import SearchVectorField
from accounts.models import MainUser


class OrderStatus(Enum):
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    description = models.TextField()
    categories = models.ManyToManyField(BookCategory, related_name='books')
    isbn = models.CharField(max_length=20, unique=True)
    page_count = models.IntegerField()
    image_links = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()
    shipping_details = models.JSONField(blank=True, null=True)
    language = models.CharField(max_length=50)
    rating = models.FloatField(null=True, blank=True)
    search_vector = SearchVectorField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def save(self, *args, **kwargs):
        # Set the search_vector only when updating, not when creating
        if self.pk:  # This means the object is being updated
            from django.contrib.postgres.search import SearchVector
            self.search_vector = (
                SearchVector('title') + SearchVector('author') + SearchVector('description')
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='orders')
    books = models.ManyToManyField(Book, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in OrderStatus],
        default=OrderStatus.PENDING.value
    )
    shipping_address = models.JSONField()  # Shipping address details
    payment_status = models.CharField(max_length=20, default='unpaid')  # Paid or Unpaid
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class Seller(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='sellers')
    store_name = models.CharField(max_length=255)
    store_description = models.TextField()
    store_logo = models.URLField(blank=True, null=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name


class SellerDashboard(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='dashboard')
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()
    total_books_sold = models.IntegerField()
    average_rating = models.FloatField()
    pending_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Dashboard for Seller {self.seller.id}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_intent_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Use decimal for accurate monetary values
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    receipt_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment {self.payment_intent_id}"


class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='inventory')
    stock_quantity = models.PositiveIntegerField()
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    warehouse_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Inventory for Book {self.book.title}"


class Review(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    helpful_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"


class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipping')
    carrier = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=255)
    shipping_date = models.DateTimeField(auto_now_add=True)
    estimated_delivery_date = models.DateTimeField()
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Shipping for Order {self.order.id}"


class Tax(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='taxes')
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tax for Order {self.order.id}"
