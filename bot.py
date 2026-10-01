import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8901508709:AAG8pG-R9I6a4e5wCrMxOAa-6DssT9ZetQ4"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "Namaskar! Bharoter jekono 10-digit mobile number pathan.\n"
        "Ami setar details khuje dichhi."
    )
    await update.message.reply_text(msg)

# Number check korar function
async def fetch_number_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num = update.message.text.strip().replace(" ", "").replace("+91", "")
    
    # Check valid 10-digit Indian number kina
    if not (num.isdigit() and len(num) == 10):
        await update.message.reply_text("❌ Kripoya ekta sothik 10-digit Indian mobile number din!")
        return

    await update.message.reply_text("🔍 Tothyo khoja hocche, ektu opekkha korun...")

    try:
        # Example API call (Apnar pawa API endpoint o key ekhane boshaban)
        # Oneke RapidAPI theke "Truecaller" ba "Indian Mobile Info" API use kore
        api_url = f"https://api.numverify.com/validate?access_key=APNAR_API_KEY&number=91{num}"
        response = requests.get(api_url).json()

        if response.get("valid"):
            operator = response.get("carrier", "Ojana")
            location = response.get("location", "India")
            line_type = response.get("line_type", "Mobile")

            reply = (
                f"📱 **Number:** +91 {num}\n"
                f"🏢 **Operator / SIM:** {operator}\n"
                f"📍 **Circle / Location:** {location}\n"
                f"📶 **Type:** {line_type}"
            )
        else:
            reply = "❌ Konono tothyo pawa jayni!"

    except Exception as e:
        reply = "⚠️️ Tothyo ante shomosya hocche. Pore chesta korun."

    await update.message.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fetch_number_info))
    
    app.run_polling()
