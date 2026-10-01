import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8901508709:AAG8pG-R9I6a4e5wCrMxOAa-6DssT9ZetQ4"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "Welcome! Nicher command gulo try korun:\n\n"
        "/info - General details\n"
        "/rules - Niyom\n"
        "/contact - Helpline"
    )
    await update.message.reply_text(msg)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📌 Amader information:\nWebsite: example.com\nService: 24/7 Active")

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 Niyomaboli:\n1. Kono spam korben na.\n2. Respectful thakun.")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Helpline: support@example.com")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("contact", contact))
    
    app.run_polling()
