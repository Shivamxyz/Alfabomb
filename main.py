import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up your Telegram Bot token
TELEGRAM_BOT_TOKEN = '6803163694:AAEQX-EYOnvjuJwNe4qwFTGUqSXJycdt0h8'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! This is your Telegram bot.')

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
