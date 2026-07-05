import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

COUPON = """
🎫 COUPON DU JOUR

⚽ Match 1 : Brazil vs Norway
➡️ +0.5 but Norway
📊 Cote : 1.41

⚽ Match 2 : Mexico vs England
➡️ -2,5 bus 
📊 Cote : 1.62

🎯 Cote totale : 2.28
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🎫 Coupon du jour"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Bienvenue 👋\nClique sur le bouton 👇",
        reply_markup=reply_markup
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🎫 Coupon du jour":
        await update.message.reply_text(COUPON)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("Bot en ligne...")
app.run_polling()
