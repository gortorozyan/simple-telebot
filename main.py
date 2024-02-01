import requests
import telebot

API_KEY = open('API_KEY').read()
SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read()
bot = telebot.TeleBot('6605728457:AAH4zd-aG0D3Px4qY_NufSbftmFRbVoL_KY')

@bot.message_handler()
def info(message):
    search_query = message.text.lower()
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'searchType': 'image'
    }
    response = requests.get(url, params=params)
    results = response.json().get('items', [])
    for item in results:
        bot.send_photo(message.chat.id, item["link"])

# Uncomment the following lines if you want to handle the '/start' command
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, "gooo")

bot.polling(none_stop=True)
