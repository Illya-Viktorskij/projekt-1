import telebot
from telebot import types
from pars import reqs
from dfg import process_sales_files
from ddec import log_message
from hh import get_token

def main():
    bot = telebot.TeleBot(get_token())
    url = "https://www.pcworld.com/article/2416915/when-the-next-steam-sale-takes-place-all-dates-at-a-glance.html"
    reqs(url=url)
    process_sales_files()

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        markup = types.InlineKeyboardMarkup()
        buttons = [
            ("Отримати знижки", "send_text"),
            ("APR", "send_text_apr"),
            ("AUG", "send_text_aug"),
            ("DEC", "send_text_dec"),
            ("FEB", "send_text_feb"),
            ("JAN", "send_text_jan"),
            ("JUL", "send_text_jul"),
            ("JUN", "send_text_jun"),
            ("MAR", "send_text_mar"),
            ("MAY", "send_text_may"),
            ("NOV", "send_text_nov"),
            ("OCT", "send_text_oct"),
            ("SEP", "send_text_sep"),
        ]

        for text, callback_data in buttons:
            markup.add(types.InlineKeyboardButton(text, callback_data=callback_data))

        bot.send_message(message.chat.id, "Натисни кнопку, щоб отримати текст:", reply_markup=markup)

    @log_message
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):

        if call.data == "send_text":
            file_path = "sale"
            send_file_content(file_path, call)

        else:
            month_mapping = {
                "send_text_apr": "month/Apr.",
                "send_text_aug": "month/Aug.",
                "send_text_dec": "month/Dec.",
                "send_text_feb": "month/Feb.",
                "send_text_jan": "month/Jan.",
                "send_text_jul": "month/Jul.",
                "send_text_jun": "month/Jun.",
                "send_text_mar": "month/Mar.",
                "send_text_may": "month/May.",
                "send_text_nov": "month/Nov.",
                "send_text_oct": "month/Oct.",
                "send_text_sep": "month/Sep.",
            }
            if call.data in month_mapping:
                print(call.data)
                print(month_mapping[call.data])
                send_file_content(month_mapping[call.data], call)

    def send_file_content(file_path, call):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            bot.send_message(call.message.chat.id, text)


    print("bot ready")
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
