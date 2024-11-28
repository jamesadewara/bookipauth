from django.db import models
from decimal import Decimal
from enum import Enum

class OrderStatus(Enum):
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'

class Order(models.Model):
    order_id = models.CharField(max_length=255, unique=True)
    customer_id = models.CharField(max_length=255)
    books = models.JSONField()  # Stores list of books with quantities
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[(status.value, status.name) for status in OrderStatus],
    default=OrderStatus.PENDING.value)
    shipping_address = models.JSONField()  # Shipping address details
    payment_status = models.CharField(max_length=20)  # Paid or Unpaid
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id}"

class Seller(models.Model):
    seller_id = models.CharField(max_length=255, unique=True)
    user_id = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    store_description = models.TextField()
    store_logo = models.URLField(blank=True, null=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name

class ProductListing(models.Model):
    product_id = models.CharField(max_length=255, unique=True)
    book_id = models.CharField(max_length=255)
    seller_id = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    shipping_details = models.JSONField()  # Shipping options
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.product_id}"

class SellerDashboard(models.Model):
    seller_id = models.CharField(max_length=255)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()
    total_books_sold = models.IntegerField()
    average_rating = models.FloatField()
    pending_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Dashboard for Seller {self.seller_id}"

class Payment(models.Model):
    payment_intent_id = models.CharField(max_length=255)
    amount = models.IntegerField()  # Amount in cents
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)
    receipt_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Payment {self.payment_intent_id}"

class Inventory(models.Model):
    book_id = models.CharField(max_length=255, unique=True)
    stock_quantity = models.IntegerField()
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    warehouse_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Inventory for Book {self.book_id}"

class Review(models.Model):
    review_id = models.CharField(max_length=255, unique=True)
    user_id = models.CharField(max_length=255)
    book_id = models.CharField(max_length=255)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    helpful_votes = models.IntegerField()

    def __str__(self):
        return f"Review {self.review_id}"

class Shipping(models.Model):
    order_id = models.CharField(max_length=255)
    shipping_address = models.JSONField()
    carrier = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=255)
    shipping_date = models.DateTimeField(auto_now_add=True)
    estimated_delivery_date = models.DateTimeField()
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Shipping for Order {self.order_id}"

class Tax(models.Model):
    order_id = models.CharField(max_length=255)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_address = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tax for Order {self.order_id}"

class Buyer(models.Model):
    buyer_id = models.CharField(max_length=255, unique=True)
    user_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Buyer {self.buyer_id}"

class BuyerDashboard(models.Model):
    buyer_id = models.CharField(max_length=255)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()
    books_purchased = models.IntegerField()
    average_rating = models.FloatField()
    wishlist = models.JSONField()

    def __str__(self):
        return f"Dashboard for Buyer {self.buyer_id}"
