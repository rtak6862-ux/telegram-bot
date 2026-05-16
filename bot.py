from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import pandas as pd

TOKEN = "8772201536:AAG6TpU04rkcKjnV_dQcpkrqfmUtK42cYpg"

# گرفتن قیمت طلا
def get_gold_price():
    url = "https://api.gold-api.com/price/XAU"
    data = requests.get(url).json()
    return float(data["price"])

# سیگنال ساده
def generate_signal(price):
    if price > 2400:
        return "🟢 BUY SIGNAL\nخرید طلا"
    elif price < 2300:
        return "🔴 SELL SIGNAL\nفروش طلا"
    else:
        return "🟡 NO SIGNAL\nفعلاً معامله نکن"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ربات سیگنال طلا فعال شد.\nدستور /gold را بزن."
    )

async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_gold_price()
    signal = generate_signal(price)

    text = f"""
📊 GOLD SIGNAL

💰 Price: {price}

{signal}
"""

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gold", gold))

print("Bot Running...")
app.run_polling()
