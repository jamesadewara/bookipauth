# Bookstore API Backend

## Overview

The Bookstore API is designed to manage a platform for buying and selling books, with features including user authentication, order management, inventory, payments, reviews, and recommendations. It allows buyers and sellers to interact within a digital bookstore ecosystem.

## Technologies Used

- **Django**: The primary web framework for the backend.
- **Django Rest Framework (DRF)**: Used for creating RESTful APIs.
- **dj-rest-auth**: For user authentication and account management.
- **django-allauth**: Provides authentication support including social login.
- **drf-yasg**: For generating Swagger UI for API documentation.
- **Stripe**: Integrated for payment processing.
- **Shippo**: Integrated for shipping and tracking orders.
- **SendGrid**: Used for email marketing and notifications.

## Models & API Endpoints

### 1. **User Authentication and Account Management API**  
**API Endpoint**: `/users`  
- Fields: `user_id`, `email`, `password`, `first_name`, `last_name`, `role`, `created_at`, `last_login`.

### 2. **Book Data API**  
**API Endpoint**: `/books`  
- Fields: `id`, `title`, `author`, `publisher`, `published_date`, `description`, `categories`, `isbn`, `page_count`, `image_links`, `language`, `rating`.

### 3. **Search API**  
**API Endpoint**: `/search`  
- Fields: `query`, `results`, `filters`, `sort`, `page`.

### 4. **Order Management API**  
**API Endpoint**: `/orders`  
- Fields: `order_id`, `customer_id`, `books`, `total_price`, `status`, `shipping_address`, `payment_status`, `order_date`.

### 5. **Seller API**  
**API Endpoint**: `/sellers`  
- Fields: `seller_id`, `user_id`, `store_name`, `store_description`, `store_logo`, `rating`, `created_at`.

### 6. **Product Listing API**  
**API Endpoint**: `/sellers/{seller_id}/products`  
- Fields: `product_id`, `book_id`, `seller_id`, `price`, `quantity_available`, `shipping_details`, `created_at`.

### 7. **Seller Dashboard API**  
**API Endpoint**: `/sellers/{seller_id}/dashboard`  
- Fields: `total_sales`, `total_orders`, `total_books_sold`, `average_rating`, `pending_orders`, `total_revenue`.

### 8. **Payment API**  
**API Endpoint**: `/payments`  
- Fields: `payment_intent_id`, `amount`, `currency`, `status`, `customer_id`, `payment_method`, `receipt_url`, `created_at`, `description`.

### 9. **Review and Ratings API**  
**API Endpoint**: `/reviews`  
- Fields: `review_id`, `user_id`, `book_id`, `rating`, `review_text`, `created_at`, `helpful_votes`.

### 10. **Inventory Management API**  
**API Endpoint**: `/inventory`  
- Fields: `book_id`, `stock_quantity`, `book_price`, `last_updated`, `warehouse_location`.

### 11. **Shipping API**  
**API Endpoint**: `/shipping`  
- Fields: `order_id`, `shipping_address`, `carrier`, `tracking_number`, `shipping_date`, `estimated_delivery_date`, `shipping_cost`.

### 12. **Tax Calculation API**  
**API Endpoint**: `/taxes`  
- Fields: `order_id`, `tax_amount`, `tax_rate`, `shipping_address`, `created_at`.

### 13. **Recommendation API**  
**API Endpoint**: `/recommendations`  
- Fields: `user_id`, `book_recommendations`, `category`, `timestamp`.

### 14. **Buyer API (Customer Account Management)**  
**API Endpoint**: `/buyers`  
- Fields: `buyer_id`, `user_id`, `first_name`, `last_name`, `email`, `created_at`, `last_login`.

### 15. **Buyer Dashboard API**  
**API Endpoint**: `/buyers/{buyer_id}/dashboard`  
- Fields: `total_spent`, `total_orders`, `books_purchased`, `average_rating`, `wishlist`.

### 16. **Email Marketing API**  
**API Endpoint**: `/emails`  
- Fields: `email_id`, `recipient_email`, `subject`, `body`, `status`, `sent_at`, `template`.

## Setup and Installation

1. **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <project-folder>
    ```

2. **Install Dependencies:**
    Make sure you have Python 3.8+ and install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations:**
    Apply database migrations:
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser (for Admin Access):**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

6. **Access API Documentation:**
    The Swagger UI for the API is available at `/swagger/`.

## Endpoints Authentication

- **Login**: Use `/users/login/` endpoint to authenticate and retrieve a token.
- **Signup**: Use `/users/signup/` to register a new user.
- **Access Protected Resources**: Use the Bearer token for all authenticated requests.

## Testing the API

You can use tools like **Postman** or **Swagger UI** (automatically generated via `drf-yasg`) to interact with the API endpoints.
