import os
import threading
from flask import Flask

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8398525143"))

# --- Render uchun mini web ---
web = Flask(__name__)

@web.get("/")
def home():
    return "Bot is running ✅", 200

# --- Bot sozlamalari ---
order_mode = {}

keyboard = [
    ["👨 Erkaklar atirlari", "👩 Ayollar atirlari"],
    ["🔥 Chegirmalar", "📦 Buyurtma berish"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# RASMLAR
IMG_DIOR_SAUVAGE = "https://elcos.uz/static/siteApp/media/f3bfe6a4-0d7a-4142-8795-025eeec8267b.jpg"
IMG_LV_IMAGINATION = "https://olcha.uz/image/700x700/products/2022-03-10/louis-vuitton-imagination-edp-u-100ml-original-39821-0.jpeg"
IMG_BLEU_DE_CHANEL = "https://olcha.uz/image/700x700/products/2022-02-07/chanel-bleu-de-chanel-edp-100ml-original-35443-0.jpeg"
IMG_GUCCI_FLORA = "https://dutyfree.uz/thumb/2/IRc9N72JVJ25TfdcZZ5qbg/r/d/2_438.jpg"
IMG_BACCARAT = "https://www.prom.uz/_ipx/f_webp/https://devel.prom.uz/upload/product_logos/77/bd/77bd370d9652e9d406d11823b98c564a.jpg"
IMG_CHANEL_CHANCE = "https://elisium.uz/thumb/2/NvF66IHxlQmn-lqMwhWOcw/r/d/chance-eau-de-toilette-spray-3-4fl-oz_packshot-default-126460-8841593683998-scale-2_00x.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\n"
        "✨ *Atirlar Dunyosi* botiga xush kelibsiz 🧴\n\n"
        "Quyidagi bo‘limlardan birini tanlang 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    if text == "👨 Erkaklar atirlari":
        await context.bot.send_photo(
            chat_id=chat_id, photo=IMG_DIOR_SAUVAGE, parse_mode="Markdown",
            caption=("🧴 *Dior Sauvage* 🌿\n━━━━━━━━━━━━━━\n"
                     "🔥 Erkaklar orasida *TOP hit*\n"
                     "🌪 Kuchli, jozibali va universal hid\n\n"
                     "💰 *Narxi:* *420,000 so‘m*\n"
                     "⏳ *Stoyka:* 8–12 soat\n"
                     "🎁 *Bonus:* bepul upakovka\n\n"
                     "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇")
        )
        await context.bot.send_photo(
            chat_id=chat_id, photo=IMG_LV_IMAGINATION, parse_mode="Markdown",
            caption=("🧴 *Louis Vuitton Imagination* 🍋\n━━━━━━━━━━━━━━\n"
                     "✨ *Fresh & luxury* segment\n"
                     "🌟 Trenddagi eng yoqimli hidlardan biri\n\n"
                     "💰 *Narxi:* *470,000 so‘m*\n"
                     "⏳ *Stoyka:* 10–12 soat\n"
                     "🚚 *Yetkazib berish:* bor\n\n"
                     "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇")
        )
        await context.bot.send_photo(
            chat_id=chat_id, photo=IMG_BLEU_DE_CHANEL, parse_mode="Markdown",
            caption=("🧴 *Bleu de Chanel* 🌊\n━━━━━━━━━━━━━━\n"
                     "🎩 Elegant & classic — *premium tanlov*\n"
                     "💎 Ofis, uchrashuv, har kuni uchun mos\n\n"
                     "💰 *Narxi:* *450,000 so‘m*\n"
                     "⏳ *Stoyka:* 8–10 soat\n"
                     "✅ *Sovg‘aga ham ideal*\n\n"
                     "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇")
        )

    elif text == "👩 Ayollar atirlari":
        await context.bot.send_photo(
            chat_id=chat_id, photo=IMG_CHANEL_CHANCE, parse_mode="Markdown",
            caption=("🌸 *Chanel Chance* 💎\n━━━━━━━━━━━━━━\n"
                     "✨ Nafis va romantik ayollar atiri\n"
                     "🌷 Yengil, yoqimli va o‘ta chiroyli aroma\n\n"
                     "💰 *Narxi:* *380,000 so‘m*\n"
                     "⏳ *Stoyka:* 6–8 soat\n"
                     "🎀 *Premium ko‘rinish*\n\n"
                     "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇")
        )
        await context.bot.send_photo(
            chat_id=chat_id, photo=IMG_GUCCI_FLORA, parse_mode="Markdown",
            caption=("🌺 *Gucci Flora* 🌷\n━━━━━━━━━━━━━━\n"
                     "💕 Gulli va yumshoq aroma\n"
                     "🌼 Juda nafis ayollar uchun tanlov\n\n"
                     "💰 *Narxi:* *360,000 so‘m*\n"
                     "⏳ *Stoyka:* 6–8 soat\n"
                     "🎁 *Sovg‘aga zo‘r*\n\n"
                     "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇")
        )
        await context.bot.send_photo(
            chat_id=chat_id, photo=IMG_BACCARAT, parse_mode="Markdown",
            caption=("🔥 *Baccarat Rouge 540* 👑\n━━━━━━━━━━━━━━\n"
                     "💎 Juda premium va mashhur hid\n"
                     "✨ Boy va jozibali aroma — *luxury effect*\n\n"
                     "💰 *Narxi:* *490,000 so‘m*\n"
                     "⏳ *Stoyka:* 12+ soat\n"
                     "🚀 *Eng kuchli variant*\n\n"
                     "📦 Buyurtma uchun: *Buyurtma berish* tugmasini bosing 👇")
        )

    elif text == "🔥 Chegirmalar":
        await update.message.reply_text(
            "🔥 *Bugungi chegirmalar* 💸\n\n"
            "✅ *Louis Vuitton Imagination* — *-20%*\n"
            "✅ *Dior Sauvage* — *-15%*\n\n"
            "⏳ Aksiya bugun amal qiladi!\n"
            "📦 Buyurtma: *Buyurtma berish* 👇",
            parse_mode="Markdown"
        )

    elif text == "📦 Buyurtma berish":
        order_mode[user_id] = True
        await update.message.reply_text(
            "📦 *Buyurtma berish* 🛒\n\n"
            "Iltimos, quyidagilarni *bitta xabarda* yuboring:\n\n"
            "👤 Ism:\n"
            "📞 Telefon:\n"
            "🧴 Qaysi atir:\n"
            "📏 Hajmi (50ml / 100ml):\n"
            "📍 Manzil:",
            parse_mode="Markdown"
        )

    elif user_id in order_mode:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🛒 Yangi buyurtma!\n\n{text}\n\n👤 User ID: {user_id}"
        )
        await update.message.reply_text(
            "✅ *Buyurtmangiz qabul qilindi!* 🎉\n⏱️ Admin tez orada bog‘lanadi.",
            parse_mode="Markdown"
        )
        del order_mode[user_id]

    else:
        await update.message.reply_text(
            "🙂 Iltimos, pastdagi *menyu tugmalari* orqali tanlang 👇",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

def run_bot():
    if not TOKEN:
        raise RuntimeError("TOKEN environment variable is missing")
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT, message_handler))
    bot_app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.getenv("PORT", "10000"))
    web.run(host="0.0.0.0", port=port)