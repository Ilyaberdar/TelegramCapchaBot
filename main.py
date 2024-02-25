import telebot
from telebot import types
from save_users import *
from region import *

with open('bot_token.txt', 'r') as file:
    bot_token = file.read().strip()

bot = telebot.TeleBot(bot_token)

user_id_global = None
chat_id_global = None

@bot.chat_join_request_handler()
def start_conversation(message):
    global user_id_global, chat_id_global

    user_id_global = message.from_user.id
    chat_id_global = message.chat.id
    user_language = message.from_user.language_code
    hello_message = switchfirstmessage_language(user_language)

    markup = types.InlineKeyboardMarkup(row_width=2)

    first_button, second_button = switchsecondmessage_language(user_language)

    apply = types.InlineKeyboardButton(first_button, callback_data="apply")
    refuse = types.InlineKeyboardButton(second_button, callback_data="refuse")
    markup.add(apply, refuse)

    try:
        bot.send_message(user_id_global, hello_message, reply_markup=markup)
    except Exception as e:
        print("ERR { in chat_join_request_handler() } : ", e)


@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        if callback.data == 'apply':
            try:
                bot.send_message(callback.message.chat.id, switchsuccsess_language(callback.from_user.language_code))
                bot.send_message(callback.message.chat.id, switchthirdmessage_language(callback.from_user.language_code))
                bot.approve_chat_join_request(chat_id_global, user_id_global)

                # save user to list
                update_user_ids('users_list.json', callback.message.chat.id)

            except Exception as e:
                print("ERR { callback_query_handler() } : ", e)

        if callback.data == 'refuse':
            try:
                bot.send_message(callback.from_user.id, "Good luck!")
            except Exception as e:
                print("ERR { callback_query_handler() } : ", e)


@bot.message_handler(commands=['send_to_all'])
def send_to_all(message):
    with open('admin_id.txt', 'r') as file:
        ADMIN_ID = int(file.read().strip())

    if message.from_user.id == ADMIN_ID:
        if len(message.text.split(maxsplit=1)) > 1:
            text_to_send = message.text.split(maxsplit=1)[1]

        for user_id in load_chat_ids('users_list.json'):
            try:
                bot.send_message(user_id, text_to_send)
            except Exception as e:
                print("ERR { callback_query_handler() } : ", e)


bot.polling()