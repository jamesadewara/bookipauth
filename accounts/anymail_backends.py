import json
import requests
from anymail.backends.base import BaseEmailBackend
from django.core.mail import EmailMessage
from django.conf import settings

class ElasticEmailBackend(BaseEmailBackend):
    """
    A custom email backend for sending emails via Elastic Email API.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = settings.ELASTIC_EMAIL_API_KEY
        self.api_url = settings.ELASTIC_EMAIL_API_URL

    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects via the Elastic Email API.
        """
        if not email_messages:
            return []

        sent_count = 0
        for message in email_messages:
            if self.send_email(message):
                sent_count += 1

        return [sent_count]

    def send_email(self, email_message: EmailMessage):
        """
        Send a single email using Elastic Email API.
        """
        subject = email_message.subject
        body = email_message.body
        from_email = email_message.from_email
        recipient_list = email_message.to

        # Prepare the data to send to Elastic Email
        data = {
            'from': from_email,
            'fromName': from_email,  # Optional: You can customize the 'fromName' field
            'to': ','.join(recipient_list),
            'subject': subject,
            'bodyText': body,  # Send plain text email body
            'apikey': self.api_key,
        }

        # Send the POST request to Elastic Email
        response = requests.post(self.api_url, data=data)

        # Check for success
        if response.status_code == 200:
            return True
        else:
            self.log_error(response)
            return False

    def log_error(self, response):
        """
        Log errors for debugging and troubleshooting.
        """
        error_message = f"Elastic Email API error: {response.status_code} - {response.text}"
        self.logger.error(error_message)
