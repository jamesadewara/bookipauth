FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /bookipauth
COPY requirements.txt /bookipauth/
RUN pip install -r requirements.txt
COPY . /bookipauth/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]