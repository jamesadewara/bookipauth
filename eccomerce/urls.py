from django.urls import path
from .views import (
    BookListCreateView, BookRetrieveUpdateDestroyView,
    BookCategoryListCreateView, BookCategoryRetrieveUpdateDestroyView,
    OrderListCreateView, OrderRetrieveUpdateDestroyView,
    SellerListCreateView, SellerRetrieveUpdateDestroyView,
    SellerDashboardListCreateView, SellerDashboardRetrieveUpdateDestroyView,
    PaymentListCreateView, PaymentRetrieveUpdateDestroyView,
    InventoryListCreateView, InventoryRetrieveUpdateDestroyView,
    ReviewListCreateView, ReviewRetrieveUpdateDestroyView,
    ShippingListCreateView, ShippingRetrieveUpdateDestroyView,
    TaxListCreateView, TaxRetrieveUpdateDestroyView
)

urlpatterns = [
    # Book URLs
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    
    # BookCategory URLs
    path('api/bookcategories/', BookCategoryListCreateView.as_view(), name='bookcategory-list-create'),
    path('api/bookcategories/<int:pk>/', BookCategoryRetrieveUpdateDestroyView.as_view(), name='bookcategory-retrieve-update-destroy'),
    
    # Order URLs
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
    
    # Seller URLs
    path('api/sellers/', SellerListCreateView.as_view(), name='seller-list-create'),
    path('api/sellers/<int:pk>/', SellerRetrieveUpdateDestroyView.as_view(), name='seller-retrieve-update-destroy'),
    
    # SellerDashboard URLs
    path('api/sellerdashboards/', SellerDashboardListCreateView.as_view(), name='sellerdashboard-list-create'),
    path('api/sellerdashboards/<int:pk>/', SellerDashboardRetrieveUpdateDestroyView.as_view(), name='sellerdashboard-retrieve-update-destroy'),
    
    # Payment URLs
    path('api/payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('api/payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-retrieve-update-destroy'),
    
    # Inventory URLs
    path('api/inventories/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('api/inventories/<int:pk>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-retrieve-update-destroy'),
    
    # Review URLs
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
    
    # Shipping URLs
    path('api/shippings/', ShippingListCreateView.as_view(), name='shipping-list-create'),
    path('api/shippings/<int:pk>/', ShippingRetrieveUpdateDestroyView.as_view(), name='shipping-retrieve-update-destroy'),
    
    # Tax URLs
    path('api/taxes/', TaxListCreateView.as_view(), name='tax-list-create'),
    path('api/taxes/<int:pk>/', TaxRetrieveUpdateDestroyView.as_view(), name='tax-retrieve-update-destroy'),
]
