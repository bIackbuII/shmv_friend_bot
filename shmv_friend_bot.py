"""
Simple Bot to reply to Telegram messages to friends.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
"""

from loguru import logger
from telegram import error
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext

logger.add('message.log', 
            format='{time} {level} {message}',
            level='INFO',
            rotation='00:00',
            compression='zip')

FRIENDS = {
    # "5299115882": "1170157639",
    # "665777296": "246509974",
    # "863710669": "628929276",
    # "502559187": "527430304",
    # "765402558": "1035656733",
    # "788424203": "1548740941",
    # "775469678": "413697443",
    # "907845493": "545017135",
    # "1082320545": "807596475",
    # "396193272": "889397017",
    # "878640627": "740025830",
    # "414544590": "519370057",
    # "937279179": "952413207",
    # "529703345": "815499143",
    # "1170157639": "5299115882",
    # "246509974": "665777296",
    # "628929276": "863710669",
    # "527430304": "502559187",
    # "1035656733": "765402558",
    # "1548740941": "788424203",
    # "413697443": "775469678",
    # "545017135": "907845493",
    # "807596475": "1082320545",
    # "889397017": "396193272",
    # "740025830": "878640627",
    # "519370057": "414544590",
    # "952413207": "937279179",
    # "815499143": "529703345",
    "878640627": "1586794973",
    "1586794973": "878640627",
}


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    chat = update.effective_chat
    if str(chat.id) in FRIENDS:
        update.message.reply_text(    
            'Привет, я буду помогать тебе связываться с твоим другом по переписке! '
            'Он уже был тебе назначен. Все сообщения, которые ты сюда напишешь, '
            'я автоматически перешлю ему. Будь осторожен с сообщениями, '
            'так как я их просто пересылаю, редактировать или изменить их потом не получится. '
            'Приятного общения)'
        )
        try:
            context.bot.send_message(chat_id=FRIENDS[str(chat.id)], text='Ваш собеседник присоединился!')
        except error.BadRequest:
            send_info(context, chat.id)
        except error.Unauthorized:
            send_warning(context, chat.id)
    else:
        update.message.reply_text('Похоже вы не зарагистрированы в системе, обратитесь к @chernovol_elisey!')
        logger.warning('Unknown user!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Если у вас возникли какие-то проблемы, напишите @chernovol_elisey.')


def about_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /about is issued."""
    update.message.reply_text(    
            'Бот был написан специально для третьей группы ШМВ-2022. '
            'Осуществляет функцию анонимного мессенджера для двух пользователей.'
        )


def send_info(context, id):
    context.bot.send_message(chat_id=id, text='Ваш собеседник еще не присоединился(')

def send_warning(context, id):
    context.bot.send_message(chat_id=id, text='Вас нет в списке участников!(')

def send_info_bot(context, id):
    context.bot.send_message(chat_id=id, text='Ваш собеседник заблокировал бота(')

def send_message(update: Update, context: CallbackContext) -> None:
    """Send to friend message."""
    chat = update.effective_chat
    try:
        if (update.message.text != None):
                context.bot.send_message(chat_id=FRIENDS[str(chat.id)], text=update.message.text)
                logger.info('{}: {}'.format(chat.id, update.message.text))
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)



def send_sticker(update: Update, context: CallbackContext) -> None:
    """Send to friend sticker."""
    chat = update.effective_chat
    try:
        if (update.message.sticker != None):
            context.bot.send_sticker(chat_id=FRIENDS[str(chat.id)], sticker=update.message.sticker)
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)


def send_voice(update: Update, context: CallbackContext) -> None:
    """Send to friend voice."""
    chat = update.effective_chat
    try:
        if (update.message.voice != None):
            context.bot.send_voice(chat_id=FRIENDS[str(chat.id)], voice=update.message.voice)
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)


def send_photo(update: Update, context: CallbackContext) -> None:
    """Send to friend user photo."""
    chat = update.effective_chat
    try:
        if (update.message.photo != None):
            context.bot.send_photo(chat_id=FRIENDS[str(chat.id)], photo=update.message.photo[0])
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)


def send_video_note(update: Update, context: CallbackContext) -> None:
    """Send to friend user video_note."""
    chat = update.effective_chat
    try:
        if (update.message.video_note != None):
            context.bot.send_video_note(chat_id=FRIENDS[str(chat.id)], video_note=update.message.video_note)
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)


def send_document(update: Update, context: CallbackContext) -> None:
    """Send to friend user document."""
    chat = update.effective_chat
    try:
        if (update.message.document != None):
            context.bot.send_document(chat_id=FRIENDS[str(chat.id)], document=update.message.document)
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)


def send_location(update: Update, context: CallbackContext) -> None:
    """Send to friend user location."""
    chat = update.effective_chat
    try:
        if (update.message.location != None):
            context.bot.send_location(chat_id=FRIENDS[str(chat.id)], location=update.message.location)
    except error.BadRequest:
        send_info(context, chat.id)
    except error.Unauthorized:
        send_info_bot(context, chat.id)
    except KeyError:
        send_warning(context, chat.id)


def main() -> None:
    """Start the bot."""
    updater = Updater("5109625593:AAFMZk9gnfB5GfQAYa2_IKm841QPI1lWETU")
    logger.info('Start server!')

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about_command))

    dispatcher.add_handler(MessageHandler(Filters.text, send_message))
    dispatcher.add_handler(MessageHandler(Filters.sticker, send_sticker))
    dispatcher.add_handler(MessageHandler(Filters.voice, send_voice))
    dispatcher.add_handler(MessageHandler(Filters.photo, send_photo))
    dispatcher.add_handler(MessageHandler(Filters.video_note, send_video_note))
    dispatcher.add_handler(MessageHandler(Filters.document, send_document))
    dispatcher.add_handler(MessageHandler(Filters.location, send_location))
    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()