# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /bookipauth

# Install system dependencies
RUN apt update && apt install -y --no-install-recommends \
    gcc libpq-dev python3-venv \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Set up the virtual environment using Python's built-in venv module
RUN python3 -m venv /bookipauth/venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/bookipauth/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the current directory contents into the container
COPY . /bookipauth/

# Install dependencies in the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000