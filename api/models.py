from django.db import models

class EmailLog(models.Model):
    """
    Stores a log of welcome emails sent to users.
    """
    username = models.CharField(max_length=150, help_text="User's username")
    email = models.EmailField(help_text="User's email address")
    sent_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the email was sent")

    def __str__(self):
        return f"Email to {self.username} ({self.email}) at {self.sent_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Email Log"
        verbose_name_plural = "Email Logs"
        ordering = ['-sent_at']  # Sort logs by most recent first
