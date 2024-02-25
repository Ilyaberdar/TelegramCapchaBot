
# Telegram Capcha Bot

Automatic reception of applications into the channel

## Installation
```bash
  pip install -r requirements.txt 
```
### Setup
1.  Open your telegram and find this bot (https://t.me/userinfobot).
Take ID and paste it into the file (admin_id.txt). This is needed to text all chats through the bot.

2.  Next, find the bot (https://t.me/BotFather) and create your own bot there.
Give your bot a name and copy its ID format ```1111111111:XXXXXX....``` then paste it into the file (bot_token.txt).

3.  Add a bot to your channel and give it admin rights.

4. Run ```main.py```

## Sending a message to all chats

Find your created bot and send it a message to send to all active chats in the format of ```/send_to_all {message}``` where "message" it's your custom text.

Example:
```/send_to_all Test message```