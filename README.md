
# Bookstore API Backend

## Overview

The **Bookstore API** is designed to manage a platform for buying and selling books. It offers features including user authentication, order management, inventory control, payments, reviews, and recommendations. The API facilitates interactions between buyers and sellers within a digital bookstore ecosystem.

## Technologies Used

- **Backend Framework**: Django powers the backend of the application.
- **API Framework**: Django Rest Framework (DRF) helps in creating RESTful APIs for communication.
- **Authentication & Account Management**: dj-rest-auth manages user authentication and account functions.
- **Social Logins**: django-allauth enables social authentication via services like Google and Facebook.
- **API Documentation**: drf-yasg generates API documentation using Swagger UI.
- **Database**: PostgreSQL is used for storing all the data.
- **CORS Handling**: django-cors-headers manages Cross-Origin Resource Sharing (CORS) to allow or restrict requests from different origins.
- **Event Handling**: Signals are used to decouple components and handle specific events.
- **Email Sending**: Elastic Email is used for transactional emails like order confirmations.
- **OAuth Authentication**: OAuth enables sign-ins using Google, Facebook, Apple, or GitHub.
- **API Performance**: Throttling controls the number of API requests to improve performance and prevent misuse.
- **Caching**: Redis is used to cache data and speed up the application.
- **Compression**: API compression is used to reduce the size of data transferred, improving response times.
- **Load Balancing**: nginx handles load balancing for production setups.
- **SSL Encryption**: SSL ensures secure communication over HTTPS in production environments.

**Note:**  
*When DEBUG is False, you should always use HTTPS (with proper SSL configurations) to ensure secure transmission of sensitive data, including user credentials.*

---

## Models & API Endpoints

### Base URL

*localhost:8000/*

The base URL of the API can be replaced with the actual server URL.  
For example, in a local development setup, the base URL could be:

---

### API Documentation

To access the API documentation, visit the following endpoint:  
**`BASE_URL/apidoc`**

---

### API Testing

To test the API, visit the following endpoint:  
**`BASE_URL/apitest`**

---

## Authentication

- The API uses **Sessions** for primary authentication, with an option for **JWT (JSON Web Tokens)** for user sign-in. After registering and logging in, you will receive an authentication token that should be included in the headers of each request.
  
  **Example Header:**  
  `Authorization: Bearer your_token_here`

---

## Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/bookstore-api.git
   cd bookstore-api
   ```

2. **Create a Virtual Environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**  
   - Ensure that PostgreSQL is installed and running.
   - Upload the `bookdb` file into your pgAdmin.

5. **Run Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (optional)**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**  
   ```bash
   python manage.py runserver
   ```

---

## Notes

- Ensure you have Redis and PostgreSQL properly set up for caching and database management.
- For testing, you can use Postman or any other API testing tool to interact with the API.

---

# Production Setup with Docker

For a production environment, you can use **Docker** to containerize the application and manage its services.

### Steps to Run in Production Mode

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/bookstore-api.git
   cd bookstore-api
   ```

2. **Build the Docker Images**  
   Run the following command to build the images based on the Dockerfile:
   ```bash
   docker-compose up --build -d
   ```

3. **Set Up Environment Variables**  
   Ensure you have the correct environment variables for the production environment, such as database credentials, API keys, etc.

4. **Start the Containers**  
   If the containers are not running, use the following command to start them:
   ```bash
   docker-compose up -d
   ```

5. **Monitor the Logs**  
   To view logs for any service, you can use:
   ```bash
   docker-compose logs -f
   ```

6. **Run Migrations in Docker**  
   Once the containers are running, you may need to apply migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

7. **Access the Application**  
   The application should now be running at `http://localhost:8000/` or a different address if deployed on a server.

---
