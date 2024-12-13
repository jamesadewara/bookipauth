# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /bookipauth

# Install system dependencies
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

# Install virtualenv
RUN pip install virtualenv

# Set up the virtual environment
RUN virtualenv /bookipauth/venv

# Set the virtualenv as the active environment
ENV VIRTUAL_ENV=/bookipauth/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the current directory contents into the container at /bookipauth
COPY . /bookipauth/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000
