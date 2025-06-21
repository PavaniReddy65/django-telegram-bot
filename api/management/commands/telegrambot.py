from django.core.management.base import BaseCommand
from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters,
    CallbackQueryHandler, CallbackContext
)
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
from api.tasks import send_welcome_email  # ✅ Import your Celery task
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load token from .env
TOKEN = config("TELEGRAM_BOT_TOKEN")

# In-memory storage for registered users
registered_users = set()

# /start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Hello! I am your Django Telegram Bot.")

# /register command handler
def register(update: Update, context: CallbackContext):
    user = update.message.from_user
    if user.id in registered_users:
        update.message.reply_text("You are already registered!")
    else:
        registered_users.add(user.id)
        update.message.reply_text(f"✅ Registered user: {user.username or user.first_name}")

# /status command handler
def status(update: Update, context: CallbackContext):
    count = len(registered_users)
    update.message.reply_text(f"📊 Currently, {count} user(s) registered.")

# /menu command handler with inline buttons
def menu(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='opt1')],
        [InlineKeyboardButton("Option 2", callback_data='opt2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please choose an option:", reply_markup=reply_markup)

# /sendemail command handler — Celery task trigger
def sendemail(update: Update, context: CallbackContext):
    tg_user = update.effective_user
    username = tg_user.username or tg_user.first_name or "unknown_user"
    email = f"{username}@example.com"  # You can update this logic as needed

    update.message.reply_text(f"📧 Sending welcome email to {email}...")

    # Trigger the Celery task
    send_welcome_email.delay(username, email)

# Callback query handler for inline buttons
def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'opt1':
        query.edit_message_text(text="You selected Option 1")
    elif query.data == 'opt2':
        query.edit_message_text(text="You selected Option 2")
    else:
        query.edit_message_text(text="Unknown option!")

# Echo handler for other text
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"You said: {update.message.text}")

class Command(BaseCommand):
    help = "Starts the Telegram bot with multiple commands and features"

    def handle(self, *args, **kwargs):
        if not TOKEN:
            self.stderr.write(self.style.ERROR("❌ TELEGRAM_BOT_TOKEN is missing or empty"))
            return

        self.stdout.write(f"🔑 Loaded token starts with: {TOKEN[:8]}... [length: {len(TOKEN)}]")

        try:
            updater = Updater(token=TOKEN, use_context=True)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❗ Bot initialization failed: {e}"))
            return

        dispatcher = updater.dispatcher

        # Register command handlers
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("register", register))
        dispatcher.add_handler(CommandHandler("status", status))
        dispatcher.add_handler(CommandHandler("menu", menu))
        dispatcher.add_handler(CommandHandler("sendemail", sendemail))  # ✅ New email command

        # Callback and message handlers
        dispatcher.add_handler(CallbackQueryHandler(button_callback))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        self.stdout.write(self.style.SUCCESS(
            "✅ Telegram bot is running... Commands: /start, /register, /status, /menu, /sendemail"
        ))

        updater.start_polling()
        updater.idle()
