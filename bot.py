import telebot

token = "7630769240:AAGphFT9nKA-G8XY1XlkT5ZvSMDkI6bk7C4"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.infinity_polling()