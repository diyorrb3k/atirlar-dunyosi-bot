from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

TOKEN = "8784742769:AAF9oEEVg_rJYdBmNPhO-NobQQPaBdyAMzs"
ADMIN_ID = 8398525143

order_mode = {}

keyboard = [
    ["👨 Erkaklar atirlari", "👩 Ayollar atirlari"],
    ["🔥 Chegirmalar", "📦 Buyurtma berish"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

IMG_DIOR_SAUVAGE = "https://elcos.uz/static/siteApp/media/f3bfe6a4-0d7a-4142-8795-025eeec8267b.jpg"
IMG_LV_IMAGINATION = "https://olcha.uz/image/700x700/products/2022-03-10/louis-vuitton-imagination-edp-u-100ml-original-39821-0.jpeg"
IMG_BLEU_DE_CHANEL = "https://olcha.uz/image/700x700/products/2022-02-07/chanel-bleu-de-chanel-edp-100ml-original-35443-0.jpeg"

IMG_GUCCI_FLORA = "https://dutyfree.uz/thumb/2/IRc9N72JVJ25TfdcZZ5qbg/r/d/2_438.jpg"
IMG_BACCARAT = "https://www.prom.uz/_ipx/f_webp/https://devel.prom.uz/upload/product_logos/77/bd/77bd370d9652e9d406d11823b98c564a.jpg"
IMG_CHANEL_CHANCE = "https://elisium.uz/thumb/2/NvF66IHxlQmn-lqMwhWOcw/r/d/chance-eau-de-toilette-spray-3-4fl-oz_packshot-default-126460-8841593683998-scale-2_00x.jpg"


def random_price():
    return f"{random.randint(300000,500000):,}".replace(",", " ")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\n"
        "✨ *Atirlar Dunyosi* botiga xush kelibsiz\n\n"
        "Quyidagi bo‘limlardan tanlang 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    if text == "👨 Erkaklar atirlari":

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_DIOR_SAUVAGE,
            caption=f"🧴 *Dior Sauvage*\n💰 Narx: {random_price()} so'm\n🔥 Erkaklar uchun TOP hit\n\n📦 Buyurtma uchun *Buyurtma berish* tugmasini bosing",
            parse_mode="Markdown"
        )

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_LV_IMAGINATION,
            caption=f"🧴 *LV Imagination*\n💰 Narx: {random_price()} so'm\n🍋 Fresh luxury hid\n\n📦 Buyurtma uchun *Buyurtma berish* tugmasini bosing",
            parse_mode="Markdown"
        )

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_BLEU_DE_CHANEL,
            caption=f"🧴 *Bleu de Chanel*\n💰 Narx: {random_price()} so'm\n🎩 Elegant classic hid\n\n📦 Buyurtma uchun *Buyurtma berish* tugmasini bosing",
            parse_mode="Markdown"
        )

    elif text == "👩 Ayollar atirlari":

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_CHANEL_CHANCE,
            caption=f"🌸 *Chanel Chance*\n💰 Narx: {random_price()} so'm\n✨ Nafis ayollar atiri",
            parse_mode="Markdown"
        )

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_GUCCI_FLORA,
            caption=f"🌺 *Gucci Flora*\n💰 Narx: {random_price()} so'm\n💕 Gulli aroma",
            parse_mode="Markdown"
        )

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMG_BACCARAT,
            caption=f"🔥 *Baccarat Rouge 540*\n💰 Narx: {random_price()} so'm\n👑 Premium atir",
            parse_mode="Markdown"
        )

    elif text == "🔥 Chegirmalar":

        await update.message.reply_text(
            "🔥 *Bugungi chegirmalar*\n\n"
            "LV Imagination — -20%\n"
            "Dior Sauvage — -15%\n\n"
            "📦 Buyurtma uchun *Buyurtma berish* tugmasini bosing",
            parse_mode="Markdown"
        )

    elif text == "📦 Buyurtma berish":

        order_mode[user_id] = True

        await update.message.reply_text(
            "📦 *Buyurtma berish*\n\n"
            "Quyidagilarni bitta xabarda yuboring:\n\n"
            "👤 Ism\n"
            "📞 Telefon\n"
            "🧴 Qaysi atir\n"
            "📏 Hajmi (50ml / 100ml)\n"
            "📍 Manzil",
            parse_mode="Markdown"
        )

    elif user_id in order_mode:

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🛒 Yangi buyurtma!\n\n{text}\n\nUser: {user_id}"
        )

        await update.message.reply_text(
            "✅ Buyurtmangiz qabul qilindi!\nAdmin tez orada siz bilan bog‘lanadi."
        )

        del order_mode[user_id]

    else:

        await update.message.reply_text(
            "🙂 Iltimos menyudan foydalaning 👇",
            reply_markup=reply_markup
        )


if __name__ == "__main__":

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    print("Bot ishga tushdi...")

    app.run_polling()
