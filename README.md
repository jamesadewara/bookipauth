# Bookstore API Backend

## Overview

The **Bookstore API** is designed to manage a platform for buying and selling books. It provides robust user authentication and authorization features, integrating various third-party APIs, and optimizing API performance for better user experience. The project is containerized using Docker for seamless deployment and scalability.

## Technologies Used

### Backend Framework
- **Django**: A high-level Python web framework that powers the backend of the application, ensuring rapid development and a clean, pragmatic design.

### API Framework
- **Django Rest Framework (DRF)**: A powerful toolkit to build Web APIs quickly, ensuring flexible and easy-to-use RESTful API communication.

### Authentication & Account Management
- **dj-rest-auth**: A robust library for handling user authentication and account management, supporting sign-up, login, and password resets.
- **django-allauth**: Integrated for social authentication, enabling users to sign up or log in using Google, Facebook, Apple, and GitHub.

### API Documentation
- **drf-yasg**: Used to automatically generate and serve interactive Swagger API documentation, making the API more understandable and testable for developers.

### Database
- **PostgreSQL**: A powerful, open-source relational database management system, used to store all application data securely.

### CORS Handling
- **django-cors-headers**: Manages Cross-Origin Resource Sharing (CORS), allowing you to specify which domains can interact with your API.

### Event Handling
- **Django Signals**: Utilized to decouple components and handle specific events in the system, enhancing modularity and maintainability.

### Email Sending
- **Elastic Email**: Integrated for sending transactional emails, such as order confirmations and notifications.

### OAuth Authentication
- **OAuth 2.0**: Enables sign-ins using social platforms like Google, Facebook, Apple, and GitHub, ensuring smooth and secure login for users.

### API Performance Optimization
- **Throttling**: Limits the number of requests to the API to avoid overload and prevent abuse.
- **Redis**: Used for caching to improve performance and reduce latency in data retrieval.
- **API Compression**: Implements data compression to reduce the size of API responses, enhancing the speed of communication.
- **Nginx**: Employed as a reverse proxy and load balancer to manage traffic effectively in production environments.

### Security Measures
- **SSL Encryption**: Ensures secure communication over HTTPS to protect sensitive data, such as user credentials.
- **JWT (JSON Web Tokens)**: Provides an additional layer of security by enabling stateless authentication using tokens.
- **Environment Variables**: Sensitive data, such as API keys and database credentials, are stored in environment variables, ensuring safe management.

---

## Models & API Endpoints

### Base URL
The base URL for local development is:


### API Testing
You can test the API endpoints at:


## Authentication

The API uses **Sessions** for primary authentication, with an option to use **JWT (JSON Web Tokens)** for user sign-in. Once authenticated, include the token in the request header.

**Example Header:**
```bash
   Authorization: Bearer your_token_here
```

#  Setup Instructions
Follow these steps to set up the application locally.

1. **Clone the Repository**
```
   git clone https://github.com/yourusername/bookstore-api.git
   cd bookstore-api
```
2. **Create a Virtual Environment**
```
   python3 -m venv venv
   source venv/bin/activate  
   # On Windows use `venv\Scripts\activate`
```
3. **Install Dependencies**
```
   pip install -r requirements.txt
```
4. **Set Up the Database**
```
   Ensure PostgreSQL is installed and running.
```
5. **Run Migrations**
```
   python manage.py makemigrations
   python manage.py migrate
```
6. **Create a Superuser (optional)**
```
   python manage.py createsuperuser
```
7. **Run the Server**
``` 
   python manage.py runserver
```

### Notes
- **Ensure Redis and PostgreSQL are properly configured for caching and database management.**
- **Use Postman or any API testing tool to interact with the API.**

---


# Production Setup with Docker
For production deployment, Docker is used to containerize the application and its dependencies. This ensures a scalable, consistent environment across all stages of development and deployment.

### Steps to Run in Production Mode
1. **Clone the Repository**
```
   git clone https://github.com/jamesadewara/bookipauth
   cd bookstore-api
```

2. **Build the Docker Images**
- Use the following command to build the Docker images:
```
   docker-compose up --build -d
```

3. **Set Up Environment Variables**
- Ensure all environment variables (database credentials, API keys, etc.) are configured in **.env or through Docker secrets.**

4. **Start the Containers**
- If the containers are not running, use this command:
```
   docker-compose up -d
```

5. **Monitor Logs**
- To monitor the logs for any service, run:
```
   docker-compose logs -f
```

6. **Run Migrations in Docker**
- After the containers are running, apply migrations:
```
   docker-compose exec web python manage.py migrate
```

7. **Access the Application**
- The app will be accessible at http://localhost:8000/ or a server IP address, depending on your hosting setup.

# Deployment with AWS
## AWS Setup
For production deployment, we recommend using Amazon Web Services (AWS) to ensure scalability and reliability.

### Launch an EC2 Instance

- Create an **EC2** instance to host the application.
- Choose an appropriate instance type based on your load expectations.
- Install Dependencies on **EC2**
- SSH into the **EC2** instance and set up the application following the setup instructions above.

### Set Up RDS for PostgreSQL

- Use Amazon RDS to host your PostgreSQL database.
- Configure the database connection settings in the .env file of your app.
- Configure Nginx
- Set up Nginx as a reverse proxy and load balancer to handle traffic. This will improve the availability of your application.

### Enable SSL
- Use **AWS ACM (AWS Certificate Manager)** to issue an **SSL certificate** and configure it on **Nginx** for **HTTPS** communication.

### Set Up S3 for Media
- Use **Amazon S3** to store media files, such as book images, ensuring scalable and secure file management.

### Monitoring and Auto-Scaling

- Set up **CloudWatch** for monitoring logs and application performance.
- Use **AWS** Auto Scaling to dynamically adjust the number of **EC2** instances based on traffic.
---

*This setup provides a robust, scalable, and secure platform for your Bookstore API, ensuring optimal performance and reliability in both development and production environments.*