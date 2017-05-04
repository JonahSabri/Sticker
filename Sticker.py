#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import util,types
import sys
import urllib
import re
import os, glob
reload(sys)
sys.setdefaultencoding("utf-8")

admin = 201704410
token = "TOKEN"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(msg):
	text = """
به ربات بکنش خوش اومدید  :)
برای دریافت آموزش کافیه به حالت اینلاین بری و چیزی ننویسی ;)"""
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("برو به حالت اینلاین",switch_inline_query=""))
	bot.send_message(msg.chat.id,text,reply_markup=markup)

@bot.message_handler(commands=['del'])
def fors(msg):
	try:
		if msg.from_user.id == admin:
			for filename in glob.glob("*.png"):
    				os.remove(filename) 
			bot.send_message(msg.chat.id, "حذف شد")
	except Exception as e:
		print e
@bot.inline_handler(lambda query: re.match("(.*)", query.query))
def inline(msg):
	try:
		if len(msg.query) == 0:
			r2 = types.InlineQueryResultArticle('1', 'آموزش', types.InputTextMessageContent('''
آموزش استفاده از ربات :

برای استفاده از این ربات شما باید در هر چتی که میخواهید استیکر را ارسال کنید یوزرنیم ربات را نوشته و سپس کلمه مورد نظر را درج کنید...
به مثال زیر توجه کنید :

@BokoneshBot علیرضا

در مثال بالا ربات اسم ؛ علیرضا ؛ را استیکر کرده و به شما ارسال میکند

توجه کنید که فقط میتوانید فارسی تایپ کنید ...

کانال : @PG_TM
نوشته شده توسط : @AnonyDev

'''))
			bot.answer_inline_query(msg.id, [r2])
		else:
			qu = msg.query
			urllib.urlopen("http://pgtm.ir/api/naga.php?name={}".format(qu))
			urllib.urlretrieve("http://pgtm.ir/api/pic.png", str(msg.from_user.id)+".png")
			filee = open(str(msg.from_user.id)+".png","rb")
			lin = bot.send_sticker(-1001092549101,filee) 
			sticker = lin.sticker.file_id
			r = types.InlineQueryResultCachedSticker('1', sticker)
			r2 = types.InlineQueryResultArticle('2', 'درباره ما', types.InputTextMessageContent('نوشته شده توسط : @AnonyDev\n\nدرکانال ما عضو شوید : @PG_TM'))
			bot.answer_inline_query(msg.id, [r, r2])

	except Exception as e:
		print e

bot.polling(True)



