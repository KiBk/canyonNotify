#!/usr/bin/env python
# pylint: disable=C0116

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# My bike check
import parser
# Config with token
import config

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# chat_id : seconds
interval_map = {}


def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Hi! Use /notify to be notified \n /unnotify to stop bein notified \n /set to set interval')


def run_check(context: CallbackContext) -> None:
    """Run the check and message if there is a change"""
    job = context.job
    if parser.update():  
        context.bot.send_message(job.context, text=parser.status())


def get_status(update: Update, _: CallbackContext) -> None:
    """Run the check and message"""
    parser.update()
    update.message.reply_text(parser.status())


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_notify(update: Update, context: CallbackContext) -> None:
    """Create a repeated job in the queue"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    # Try to find interval
    try:
        interval = interval_map[chat_id]
    except:
        interval = config.interval
    context.job_queue.run_repeating(run_check, interval=interval,
        context=chat_id, name=str(chat_id))

    text = 'Notify was succesfully restarted!' if job_removed \
        else 'Notify was succesfully started!'
    update.message.reply_text(text)


def set_interval(update: Update, context: CallbackContext) -> None:
    """Modify the check interval"""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the interval in seconds
        interval = int(context.args[0])
        if interval < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        interval_map[chat_id] = interval

        text = f'Interval successfully set to {interval}!'
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

    # Restart notify
    set_notify(update, context)


def unset_notify(update: Update, context: CallbackContext) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Notify successfully cancelled!' if job_removed else 'You have no active notify.'
    update.message.reply_text(text)


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("set", set_interval))
    dispatcher.add_handler(CommandHandler("notify", set_notify))
    dispatcher.add_handler(CommandHandler("status", get_status))
    dispatcher.add_handler(CommandHandler("unnotify", unset_notify))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
