import telebot, getpass

user = getpass.getuser()

# Enter token code here
token = "enter token code here"

bot = telebot.TeleBot(token)

message = "Neuer Login auf Laptop Arbeitsviech - Username: " + user

# Enter chat_id here
bot.send_message("Use Telegram @getidsbot to get your personal chat id", message)

# And don't forget to make this file executable: `sudo chmod +x notifier.py`