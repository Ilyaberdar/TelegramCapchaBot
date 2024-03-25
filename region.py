def switchfirstmessage_language(user_language):
    if user_language == 'ru':
        return "Пожалуйста подтвердите что вы не робот!"
    if user_language == 'ua':
        return "Будь ласка, підтвердіть, що ви не робот!"
    else:
        return "Please confirm that you are not a robot!"

def switchsecondmessage_language(user_language):
    if user_language == 'ru':
        return "Я не робот✅", "Отказаться🚫"
    if user_language == 'ua':
        return "Я не робот✅", "Відмовитися🚫"
    else:
        return "I'm not robot✅", "Quit🚫"
    
def switchthirdmessage_language(user_language):
    if user_language == 'ru':
        return "Рад приветствовать тебя в своей группе! Заходи, располагайся🤝🏽 «https://t.me/+SHoc5FS9feZiMTZk»"
    if user_language == 'ua':
        return "Радий вітати тебе у своїй групі! Заходь, розташовуйся🤝🏽 «https://t.me/+SHoc5FS9feZiMTZk»"
    else:
        return "Glad to welcome you to my group! Come on in, make yourself comfortable🤝🏽 «https://t.me/+SHoc5FS9feZiMTZk»"
    
def switchsuccsess_language(user_language):
    if user_language == 'ru':
        return "Успешно✅"
    if user_language == 'ua':
        return "Успішно✅"
    else:
        return "Success✅"
