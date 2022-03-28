#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

USER_ID = {
    "Брайнин" : "765402558",
    "Иванцова" : "952413207",
    "Ильина" : "937279179",
    "Казаринова" : "863710669",
    "Калашникова" : "",
    "Качалова" : "246509974",
    "Ким" : "545017135",
    "Кишкурно" : "815499143",
    "Климова" : "413697443",
    "Коляда" : "807596475",
    "Кудинов" : "414544590",
    "Миночкина" : "5299115882",
    "Некозырева" : "1082320545",
    "Одинцов" : "1170157639",
    "Пухкан" : "1035656733",
    "Пчелко" : "889397017",
    "Сергеев" : "775469678",
    "Сергеева" : "502559187",
    "Шакаров" : "527430304",
    "Шалимова" : "665777296",
    "Шилкова" : "529703345",
    "Якимова" : "1548740941",
    "Балабойко" : "740025830",
    "Галицина" : "907845493",
    "Минакова" : "396193272",
    "КомароваД" : "628929276",
    "КомароваК" : "519370057",
    "Черновол" : "878640627",
    "AJurjewna": "1586794973"
}

TEST_FRIENDS = {
    # "878640627" : "1586794973",
    # "1586794973": "878640627",
    "878640627" : "740025830",
    "628929276" : "907845493",
    "519370057" : "396193272",
    "907845493" : "628929276",
    "396193272" : "519370057",
    "740025830" : "878640627",
}

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    # update.message.reply_text(
    #     'Привет, я буду помагать тебе связываться с твоим другом по переписке!'
    #     'Он уже был тебе назначен. Как только ты захочешь с ним связаться, '
    #     'отправь мне команду /message и следом сообщение.'
    # )
    update.message.reply_text(    
        'Привет, я буду помагать тебе связываться с твоим другом по переписке! '
        'Он уже был тебе назначен. Все сообщения, которые ты сюда напишешь, '
        'я автоматически перешлю ему. Приятного общения)'
        )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Если у вас возникли какие-то проблемы, напишите @chernovol_elisey!')


def send_message(update: Update, context: CallbackContext) -> None:
    """Send message for friend."""
    chat = update.effective_chat
    context.bot.send_message(chat_id=TEST_FRIENDS[str(chat.id)], text=update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5284229247:AAE8HFDVvgUUhl7cNWZ7GW3rjI7zXWaMJWA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, send_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()