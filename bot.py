import telebot
import random
import logging
import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter
from stopgame import StopGame
 
from telebot import types

bot = telebot.TeleBot('1659499007:AAHaxMj93-tJXcMqQrZ8PhP5_H-uM_RHNKs')
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("/start")
    item4 = types.KeyboardButton("Дай чит")
    item5 = types.KeyboardButton("/subscribe")
 
    markup.add(item1, item2, item3, item4, item5)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Го в кс мм или напы?", callback_data='good')
            item2 = types.InlineKeyboardButton("Нехочу, кс надоела", callback_data='bad')
            item3 = types.InlineKeyboardButton("Го по легиту в мм", callback_data='go')
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == 'Дай чит':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Инструкция по установке',callback_data='hack')

            markup.add(item1)

            bot.send_message(message.chat.id, 'https://anonfiles.com/J540a1J8se/cheats_rar',reply_markup=markup)    
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢',)

    
            
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Пошли A2EQW-L4TJ 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'go':
                bot.send_message(call.message.chat.id, 'go A2EQW-L4TJ')  
            elif call.data == 'hack':
                bot.send_message(call.message.chat.id, 'Инструкция по установке:\n1. Зайти в стим и включить VAC-Bypass-Loader.exe.\n2. Зайти в игру и с помощью CSGhost_v2.4.exe заинжектить otc3.\n3. Зайти в папку с игрой и там открыть папку ot, туда перекинуть папку scripts и leg1t.cfg,pusto.cfg.')      
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)


    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
