from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8800531130:AAEil87ibT4pmUpOTg7Er8ebRty_vpwOyV4"
CHANNEL = "@vibesof23"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        msg = int(context.args[0])
        await context.bot.copy_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL,
            message_id=msg
        )
    else:
        await update.message.reply_text("لینک نامعتبر است.")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.forward_origin:
        await update.message.reply_text(
            f"Message ID: {update.message.forward_origin.message_id}"
        )
    else:
        await update.message.reply_text("پیام را از کانال فوروارد کن.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, get_id))

print("Bot Started")
app.run_polling()
