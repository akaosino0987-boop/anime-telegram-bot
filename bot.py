from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎌 Welcome to Anime Updates Bot!\n\n"
        "Commands:\n"
        "/anime - Latest anime updates\n"
        "/onepiece - One Piece updates\n"
        "/news - Anime news"
    )

async def anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Latest Anime Updates:\n"
        "- New episodes coming soon!\n"
        "- Stay tuned 🎉"
    )

async def onepiece(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏴‍☠️ One Piece Update:\n"
        "New episode info will be posted here!"
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 Anime News:\n"
        "- New seasons announced\n"
        "- Upcoming anime releases"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("anime", anime))
    app.add_handler(CommandHandler("onepiece", onepiece))
    app.add_handler(CommandHandler("news", news))

    print("Bot is running...")
    app.run_polling()
