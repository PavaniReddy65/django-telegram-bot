from telegram.ext import CommandHandler
from .tasks import send_welcome_email  # Adjust path if needed

def sendemail_command(update, context):
    tg_user = update.effective_user
    username = tg_user.username or tg_user.first_name or "unknown_user"
    email = f"{username}@example.com"  # Replace with real logic

    update.message.reply_text(f"📧 Sending welcome email to {email}...")

    send_welcome_email.delay(username, email)
