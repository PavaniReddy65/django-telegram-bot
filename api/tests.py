from django.test import TestCase
from celery import shared_task

# Create your tests here.


@shared_task
def send_welcome_email(username, email):
    print(f"Sending welcome email to {username} at {email}")
    return f"Welcome email sent to {email}"
