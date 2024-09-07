import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from btn import *

BOT_TOKEN = "7025058195:AAEYb7A6mWX1r3ki8VrG39x59n5z5TW2xu4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
  await dp.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
    ]
  )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await message.answer("Buyurtmani birga joylashtiramizmi? 🤗"),
  await message.answer("""uyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

Oqtepa Lavash menu (https://telegra.ph/Taomnoma-09-30)

Telegraph (https://telegra.ph/Taomnoma-09-30)
Taomnoma
Buyurtma bering Buyurtma bering 📲 Biz Telegramda 📸 Biz Instagramda 👥 Biz Facebookda 📞 Aloqa uchun: 78 150 0030""",reply_markup=menu_btn)




@dp.message_handler(commands=['🛒Buyurtma berish'])
async def Buyurtma_berish(message: types.Message):
  await message.answer("Buyurtmani birga joylashtiramizmi? 🤗"),
  await message.answer("Buyurtma turini tanlang",reply_markup=menu_buyurtma),





@dp.message_handler(commands=['ℹ️ Biz haqimizda'])
async def Biz_Haqimizda(message: types.Message):
  await message.answer("Buyurtmani birga joylashtiramizmi? 🤗"),
  await message.answer("""Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.

Qaynoqqina va mazali lavashlarimiz, shaurmayu donerlarimiz, gamburger va pitsalarimizdan albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!

Yetkazib berish xizmati:  +998781500030
Sayt (https://oqtepalavash.uz/) | Facebook (http://fb.me/oqtepalavash.official) | Instagram (https://www.instagram.com/oqtepalavash.official)

Facebook (http://fb.me/oqtepalavash.official)
Log in or sign up to view
See posts, photos and more on Facebook."""),



@dp.message_handler(commands=['🛍Buyurtmalar'])
async def Buyurtma(message: types.Message):
  await message.answer("Buyurtmani birga joylashtiramizmi? 🤗"),
  await message.answer("Siz hali hanuz birorta ham buyurtma bermagansiz"),


@dp.message_handler(commands=['🏘Filialar'])
async def Filtr_handler(message: types.Message):
  await message.answer("Buyurtmani birga joylashtiramizmi? 🤗"),
  await message.answer("Bizning filiallarimiz : 65 (1-10)",reply_markup=menu_filtr),


@dp.message_handler(text="Ortga")
async def back_handler(message: types.Message):
  await message.answer(text="Bosh menu", reply_markup=menu_buyurtma)

 


if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)