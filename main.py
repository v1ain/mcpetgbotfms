from mcstatus.bedrock import BedrockServer
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

SERVER_IP = "138.201.48.55"
SERVER_PORT = 19107

async def check_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        server = BedrockServer.lookup(f"{SERVER_IP}:{SERVER_PORT}")
        status = server.status()
        await update.message.reply_text(
            f"✅ Сервер запущен!\nИгроков онлайн: {status.players_online}"
        )
    except Exception:
        await update.message.reply_text("❌ Сервер не запущен или недоступен.")

app = ApplicationBuilder().token("7939706914:AAGzUN-qmzIOTbulKa2WaHKuvdpRWtP82hc").build()
app.add_handler(CommandHandler("check", check_server))
app.run_polling()
