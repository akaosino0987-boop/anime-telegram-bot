from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

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

# -------- Main --------
app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
