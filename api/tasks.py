from celery import shared_task
import logging
import time
from django.utils.timezone import now
from .models import EmailLog  # Make sure EmailLog is defined correctly

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_welcome_email(self, username, email):
    try:
        # Log the start of the email send
        logger.info(f"📤 Sending welcome email to {username} <{email}>")
        
        # Simulate delay (e.g., sending email)
        time.sleep(2)

        # Save the log to the database
        EmailLog.objects.create(username=username, email=email, sent_at=now())

        logger.info(f"✅ Email successfully sent to {email}")
        return f"Welcome email sent to {email}"
    
    except Exception as e:
        logger.error(f"❌ Failed to send email to {email}: {str(e)}")
        self.retry(exc=e, countdown=5, max_retries=3)
