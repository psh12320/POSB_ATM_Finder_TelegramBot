# import os
# import sys
# import urllib3
# from urllib.request import urlopen
from telegram.ext import Updater, CommandHandler, Dispatcher, MessageHandler, Filters, CallbackContext, updater
from telegram import Update, ForceReply

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    update.message.reply_text("Welcome! I can find the nearest POSB ATM from your location!")


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the /help command is issued."""
    update.message.reply_text("Share your location with me and I'll find the closest POSB ATM near you!")


def location_finder(update: Update, context: CallbackContext) -> None:
    """Find user's location using the shared location on Telegram."""

def main() -> None:
    updater = Updater()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
