import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "YOUR_NEW_TOKEN_HERE"
CHANNEL = "@vibesof23"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("لینک نامعتبر است.")
        return

    try:
        message_id = int(context.args[0])

        await context.bot.copy_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL,
            message_id=message_id
        )

    except Exception as e:
        await update.message.reply_text(
            f"خطا:\n{e}"
        )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.forward_origin:
        await update.message.reply_text(
            f"Message ID: {update.message.forward_origin.message_id}"
        )
    else:
        await update.message.reply_text(
            "یک پیام از کانال فوروارد کن."
        )


async def run():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, get_id))

    print("Bot Started")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(run())
