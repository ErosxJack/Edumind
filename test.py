from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Define chatbot response function
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm good!",
        "your name": "I'm a chatbot!",
        "bye": "Goodbye!"
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

# Function to handle messages
async def handle_message(update: Update, context) -> None:
    user_input = update.message.text
    bot_response = chatbot_response(user_input)
    await update.message.reply_text(bot_response)

# Function to start the bot
async def start(update: Update, context) -> None:
    await update.message.reply_text("Hello! I'm your chatbot. Type something to chat!")

# Main function to run the bot
def main():
    TOKEN = "7349071486:AAEe_DNLF5aVOirVd0OjZPsp9idXhPoY2ZQ"  # Replace with your Telegram bot token
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
