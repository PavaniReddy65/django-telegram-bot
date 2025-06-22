# telegram_bot.py

import logging
from telegram.ext import Updater, CommandHandler
from decouple import config

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load token from environment
TOKEN = config("TELEGRAM_BOT_TOKEN")

# Define /start command behavior
def start(update, context):
    user = update.effective_user
    update.message.reply_text(f"👋 Hello {user.first_name}! I am your Django Telegram Bot. Type /help to get started.")

# Optional: Define a /help command
def help_command(update, context):
    update.message.reply_text("Available commands:\n/start - Greet the user\n/help - Show help")

# Start the bot
def main():
    # Set up the Updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start the bot
    logger.info("🚀 Telegram bot started. Waiting for commands...")
    updater.start_polling()
    updater.idle()

# Entry point
if __name__ == "__main__":
    main()
