from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

BOT_TOKEN = "8437351423:AAEauPmc30yXlTI0TstB3m2cmy-0PGrrpXk"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# In-memory storage for testing
user_data = {}

# Start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"stars": 0, "level": 1}
    await message.reply(
        f"🎉 Welcome {message.from_user.first_name}!\n"
        f"💎 Stars: {user_data[user_id]['stars']}\n"
        f"🎁 Open your gift box with /receive"
    )

# Profile command
@dp.message_handler(commands=['profile'])
async def profile(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_data:
        await message.reply(
            f"🎯 Profile:\n"
            f"💎 Stars: {user_data[user_id]['stars']}\n"
            f"🏆 Level: {user_data[user_id]['level']}"
        )
    else:
        await message.reply("No data found. Use /start first.")

# Receive gift (simulate Telegram Stars)
@dp.message_handler(commands=['receive'])
async def receive_gift(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"stars": 0, "level": 1}

    # Simulate gift box animation
    for frame in ["🎁", "🎁✨", "🎁💎", "💎💎"]:
        await message.reply(frame)
        await asyncio.sleep(0.5)

    # Add stars
    stars_received = 50
    user_data[user_id]["stars"] += stars_received

    # Check level up
    if user_data[user_id]["stars"] >= user_data[user_id]["level"] * 100:
        user_data[user_id]["level"] += 1
        await message.reply(f"⭐ Congratulations! You leveled up to Level {user_data[user_id]['level']}!")

    await message.reply(f"✅ Gift received! {stars_received} Stars added.\n💎 Total Stars: {user_data[user_id]['stars']}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)