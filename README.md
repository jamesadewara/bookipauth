# Bookstore API Backend

## Overview

The **Bookstore API** is designed to manage a platform for buying and selling books. It offers features including user authentication, order management, inventory control, payments, reviews, and recommendations. The API facilitates interactions between buyers and sellers within a digital bookstore ecosystem.

## Technologies Used

- **Django**: The primary web framework for the backend.
- **Django Rest Framework (DRF)**: Used for building RESTful APIs.
- **dj-rest-auth**: For user authentication and account management.
- **django-allauth**: Provides support for social logins and authentication.
- **drf-yasg**: For generating Swagger UI for API documentation.
- **PostgreSQL**: The database used to store data.
- **django-cors-headers**: A Django app for handling Cross-Origin Resource Sharing (CORS), which is essential for allowing or restricting requests from other domains to your backend. It is particularly useful when your frontend is hosted on a different domain or port than the backend.

**Note:**
*When DEBUG is False, you should never be using HTTP connections without proper SSL configurations to ensure sensitive data, including user credentials, are securely transmitted.*


## Models & API Endpoints

### Base URL
*localhost:8000/*

The base URL of the API can be replaced with the actual server URL.  
For example, in a local development setup, the base URL could be:

---

### API Documentation
To access the API documentation, visit the following endpoint:
***BASE_URL**/apidoc*

---

### API Testing
To test the API, visit the following endpoint:

***BASE_URL**/apitest*

---

### Models

- **User**: Represents the registered user (both buyers and sellers).
- **Book**: Represents books available for sale or purchase.
- **Order**: Represents an order made by a buyer.
- **Payment**: Represents the payment details for an order.
- **Review**: Represents reviews for books made by buyers.
- **Seller**: Represents sellers who own books listed on the platform.
- **Shipping**: Represents the shipping information related to an order.
- **Tax**: Represents the tax information for an order.
- **Inventory**: Represents the stock of books in the warehouse.
- **BookCategory**: Represents the categories for classifying books.

### API Endpoints (Sample)

- **POST /api/register/**: Register a new user.
- **POST /api/login/**: Login and receive a token.
- **GET /api/books/**: Get a list of books.
- **GET /api/books/{id}/**: Get details for a specific book.
- **POST /api/orders/**: Create a new order.
- **GET /api/orders/{id}/**: Get details of a specific order.
- **POST /api/reviews/**: Create a new review for a book.

## Authentication

- The API uses **JWT (JSON Web Tokens)** for authentication. After registering and logging in, you will receive an authentication token that should be included in the headers of each request.
- **Example Header**:  
  `Authorization: Bearer your_token_here`

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bookstore-api.git
   cd bookstore-api
2. **Create a Virtual Environment**
    ```python3 -m venv venv
    source venv/bin/activate  
    # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
    ```
    pip install -r requirements.txt
4. **Set Up the Database**
    - Ensure that PostgreSQL is installed and running.
    - Upload the bookdb file into your pgadmin
5. **Run Migrations**
    ```
    python manage.py makeigrations
    python manage.py migrate
6. **Create a Superuser (optional)**
    ```
    python manage.py createsuperuser
7. **Run the Server**
    ```
    python manage.py runserver

"# bookipauth" 
