import telebot
import requests
bot = telebot.TeleBot('1215897966:AAHIUxjTr-6gWsOO8ScL_Z_5gFtmHUBqyGE')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши число, и я напишу если о нем интересный факт")
    else:
        if message.text.isdigit():
            api_url = "http://numbersapi.com/" + message.text + "/math?json=true"
            res = requests.get(api_url)
            data = res.json()
            bot.send_message(message.from_user.id, data['text'])
        else:
            bot.send_message(message.from_user.id, "Принимаю только цифры")
bot.polling(none_stop=True, interval = 0)

