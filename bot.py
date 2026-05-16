
from telegram.ext import Application, CommandHandler

TOKEN = "8870873326:AAHBvCp1Koy45_TxAC2_pkxMKWGI815vdxw"

async def start(update, context):
    await update.message.reply_text("ربات روشن است")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("STARTED")

app.run_polling()
