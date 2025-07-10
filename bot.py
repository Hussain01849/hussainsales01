import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot Configuration - USING YOUR PROVIDED TOKEN
BOT_TOKEN = "7977009050:AAF0GXttHdo6zp7VpVnQaHcttRRIlk4aVwM"
CHANNEL_USERNAME = "@YourActualChannel"  # ⚠️ REPLACE WITH YOUR TELEGRAM CHANNEL
TWITTER_USERNAME = "@YourActualTwitter"  # ⚠️ REPLACE WITH YOUR TWITTER HANDLE

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with airdrop instructions"""
    user = update.effective_user
    welcome_msg = (
        f"👋 Hey {user.first_name}!\n\n"
        "💰 Join our crypto airdrop and get 10 SOL!\n\n"
        f"1. Join our Telegram channel: {CHANNEL_USERNAME}\n"
        f"2. Follow our Twitter: {TWITTER_USERNAME}\n\n"
        "📥 Send your Solana wallet address now!"
    )
    await update.message.reply_text(welcome_msg)

async def handle_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process 'wallet address' and send confirmation"""
    wallet = update.message.text.strip()
    solscan_link = f"https://solscan.io/account/{wallet}"
    
    response = (
        "🎉 Congratulations!\n\n"
        f"10 SOL has been sent to your wallet:\n`{wallet}`\n\n"
        f"Track transaction on [Solscan]({solscan_link})\n\n"
        "⚠️ Note: This is a test simulation. No actual SOL will be sent."
    )
    
    await update.message.reply_text(response, parse_mode="Markdown")

async def handle_invalid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle non-text inputs"""
    await update.message.reply_text("❌ Please send a valid Solana wallet address after using /start")

def main() -> None:
    """Start the bot"""
    # Create Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    application.add_handler(MessageHandler(filters.ALL, handle_invalid))
    
    # Run bot
    logger.info("Starting bot...")
    print("✅ Bot is running. Press CTRL+C to stop")
    application.run_polling()

if __name__ == "__main__":
    main()
