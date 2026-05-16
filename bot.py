
from telegram.ext import Application, CommandHandler

TOKEN = "8772201536:AAG6TpU04rkcKjnV_dQcpkrqfmUtK42cYpg"

async def start(update, context):
    await update.message.reply_text("سلام")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
