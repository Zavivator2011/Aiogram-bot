from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

menu_btn = ReplyKeyboardMarkup(resize_keyboard=True)
menu_btn.row("🛒Buyurtma berish"),
menu_btn.row("ℹ️ Biz haqimizda","🛍Buyurtmalar"),
menu_btn.row("🏘Filialar"),
menu_btn.row("✍️ Fikir bildirish","⚙️Sozlamalar")


menu_filtr = InlineKeyboardMarkup(resize_keyboard=True)
menu_filtr.row("Asosiy manu","Eng yaqin filial"),
menu_filtr.row("Keyingi"),
menu_filtr.row("Algoritm","Andijon"),
menu_filtr.row("Andijon2","Avisozlar brozi"),
menu_filtr.row("Beruniy","Bodomzor"),
menu_filtr.row("Chigatoy","Chinonzor"),
menu_filtr.row("Chilonzor-19","CHinoz"),


menu_buyurtma = ReplyKeyboardMarkup(resize_keyboard=True)
menu_buyurtma.row("Eltib berish","Borib olish"),
menu_buyurtma.row("Ortga")