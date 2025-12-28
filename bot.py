from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Anime Updates", callback_data="anime")],
        [InlineKeyboardButton("🏴‍☠️ One Piece", callback_data="onepiece")],
        [InlineKeyboardButton("📰 Anime News", callback_data="news")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎌 Welcome to Anime Updates Bot!\nChoose an option below:",
        reply_markup=reply_markup
    )

-- Button Handler --

from telegram.ext import CallbackQueryHandler

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "anime":
        await query.edit_message_text("🔥 Latest Anime updates coming soon!")
    elif query.data == "onepiece":
        await query.edit_message_text("🏴‍☠️ One Piece latest episode updates coming soon!")
    elif query.data == "news":
        await query.edit_message_text("📰 Latest anime news will be posted here!")
