#!/usr/bin/env python
# -*- coding: utf-8 -*-
bot_TOKEN = ""

from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi! /t and letter to troll. (eg. /t o sanane)\n'
                              'or you can just reply to message with /t and letter (/t o)')

def about(bot, update):
    update.message.reply_text('To advice us:\n'
                      'https://github.com/omergulen/SononoGEN/\n'
                      'or\n'
                      'omrglen@gmail.com\n'
                      'Thanks for support!')


def translator(bot, update, args):
    vovals = "aeıiuüoöAEIİUÜOÖ"
    voval = args[0] * 8 + args[0].upper() * 8
    text = " ".join(args[1:])
    translation = str.maketrans(vovals, voval)

    try:
        update.message.reply_text(update.message.reply_to_message['text'].translate(translation))
    except:
        update.message.reply_text(text.translate(translation))


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater(bot_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("t", translator,
                                  pass_args=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
