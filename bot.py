import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@newanimedaily"

# -------- Button handler --------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "anime":
        await query.edit_message_text("Latest anime episodes 🔥")
    elif query.data == "onepiece":
        await query.edit_message_text("One Piece updates ☠️")
    elif query.data == "news":
        await query.edit_message_text("Anime news 📰")

# -------- Start command --------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎌 Anime", callback_data="anime")],
        [InlineKeyboardButton("🏴‍☠️ One Piece", callback_data="onepiece")],
        [InlineKeyboardButton("📰 News", callback_data="news")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Choose an option:",
        reply_markup=reply_markup
    )

# -------- Auto Post Function --------
async def auto_post(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text="🔥 New Anime Update!\nStay tuned for latest episodes 🎌"
    )

# -------- Main --------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

job_queue = app.job_queue
job_queue.run_repeating(auto_post, interval=21600, first=10)

app.run_polling()
