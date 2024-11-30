from django.contrib import admin
from .models import (
    Book, BookCategory, Order, Seller, SellerDashboard, Payment,
    Inventory, Review, Shipping, Tax
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'published_date', 'rating')
    search_fields = ('title', 'author', 'publisher')


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'order_date')
    search_fields = ('customer__username', 'status')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'store_name', 'rating')
    search_fields = ('store_name',)


@admin.register(SellerDashboard)
class SellerDashboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'total_sales', 'average_rating')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'status')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'stock_quantity')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'rating', 'created_at')


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'carrier', 'tracking_number', 'shipping_date')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'tax_amount')
