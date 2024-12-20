# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /bookipauth

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django
EXPOSE 8000

# Run the application
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]