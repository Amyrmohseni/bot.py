import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "YOUR_NEW_TOKEN_HERE"
CHANNEL = "@vibesof23"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        try:
            msg_id = int(context.args[0])

            await context.bot.copy_message(
                chat_id=update.effective_chat.id,
                from_chat_id=CHANNEL,
                message_id=msg_id
            )

        except Exception as e:
            await update.message.reply_text(
                f"خطا در ارسال پیام:\n{e}"
            )

    else:
        await update.message.reply_text(
            "لینک نامعتبر است."
        )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.forward_origin:
        await update.message.reply_text(
            f"Message ID: {update.message.forward_origin.message_id}"
        )
    else:
        await update.message.reply_text(
            "یک پیام را از کانال فوروارد کن."
        )


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(filters.ALL, get_id)
    )

    print("Bot Started")

    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
