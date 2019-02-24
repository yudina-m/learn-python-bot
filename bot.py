from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

# Setup
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Functions
def greet_user(bot, update):
    text = 'Called /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Hello {}! You wrote: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", 
                update.message.chat.username, 
                update.message.chat.id, 
                update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Starting Telegram bot...')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

# Call
main()