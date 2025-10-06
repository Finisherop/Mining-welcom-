import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

# Initialize bot and dispatcher
try:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
except Exception as e:
    logging.error(f"Failed to initialize bot: {e}")
    raise

# In-memory storage
user_data = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    try:
        user_id = message.from_user.id
        if user_id not in user_data:
            user_data[user_id] = {"stars": 0, "level": 1}
        
        first_name = message.from_user.first_name or "User"
        await message.reply(
            f"🎉 Welcome {first_name}!\n"
            f"💎 Stars: {user_data[user_id]['stars']}\n"
            f"🎁 Open your gift box with /receive"
        )
    except Exception as e:
        logging.error(f"Error in start command: {e}")
        await message.reply("Sorry, something went wrong. Please try again.")

@dp.message(Command("profile"))
async def profile(message: types.Message):
    try:
        user_id = message.from_user.id
        if user_id in user_data:
            await message.reply(
                f"🎯 Profile:\n"
                f"💎 Stars: {user_data[user_id]['stars']}\n"
                f"🏆 Level: {user_data[user_id]['level']}"
            )
        else:
            await message.reply("No data found. Use /start first.")
    except Exception as e:
        logging.error(f"Error in profile command: {e}")
        await message.reply("Sorry, something went wrong. Please try again.")

@dp.message(Command("receive"))
async def receive_gift(message: types.Message):
    try:
        user_id = message.from_user.id
        if user_id not in user_data:
            user_data[user_id] = {"stars": 0, "level": 1}

        # Simulate gift box animation with a single message that gets edited
        animation_msg = await message.reply("🎁")
        
        for frame in ["🎁✨", "🎁💎", "💎💎"]:
            await asyncio.sleep(0.5)
            try:
                await animation_msg.edit_text(frame)
            except Exception as e:
                logging.warning(f"Failed to edit message: {e}")
                # If editing fails, send a new message
                await message.reply(frame)
                break

        # Add stars
        stars_received = 50
        user_data[user_id]["stars"] += stars_received

        # Check level up
        level_up_message = ""
        if user_data[user_id]["stars"] >= user_data[user_id]["level"] * 100:
            user_data[user_id]["level"] += 1
            level_up_message = f"\n⭐ Congratulations! You leveled up to Level {user_data[user_id]['level']}!"

        await message.reply(
            f"✅ Gift received! {stars_received} Stars added.\n"
            f"💎 Total Stars: {user_data[user_id]['stars']}"
            f"{level_up_message}"
        )
    except Exception as e:
        logging.error(f"Error in receive command: {e}")
        await message.reply("Sorry, something went wrong. Please try again.")

async def main():
    """Main function to start the bot"""
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error starting bot: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
