def switchfirstmessage_language(user_language):
    if user_language == 'ru':
        return "Пожалуйста подтвердите что вы не робот!"
    if user_language == 'en':
        return "Please confirm that you are not a robot!"
    if user_language == 'ua':
        return "Будь ласка, підтвердіть, що ви не робот!"

def switchsecondmessage_language(user_language):
    if user_language == 'ru':
        return "Я не робот✅", "Отказаться🚫"
    if user_language == 'en':
        return "I'm not robot✅", "Quit🚫"
    if user_language == 'ua':
        return "Я не робот✅", "Відмовитися🚫"
    
def switchthirdmessage_language(user_language):
    if user_language == 'ru':
        return "Рад приветствовать тебя в своей группе! Заходи, располагайся🤝🏽 «https://t.me/+ijvIVKQBWY81YmVi»"
    if user_language == 'en':
        return "Glad to welcome you to my group! Come on in, make yourself comfortable🤝🏽 «https://t.me/+ijvIVKQBWY81YmVi»"
    if user_language == 'ua':
        return "Радий вітати тебе у своїй групі! Заходь, розташовуйся🤝🏽 «https://t.me/+ijvIVKQBWY81YmVi»"
    
def switchsuccsess_language(user_language):
    if user_language == 'ru':
        return "Успешно✅"
    if user_language == 'en':
        return "Success✅"
    if user_language == 'ua':
        return "Успішно✅"
