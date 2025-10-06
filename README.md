# Telegram Star Bot

A simple Telegram bot that allows users to collect stars and level up.

## Features

- `/start` - Initialize user profile and display welcome message
- `/profile` - View current stars and level
- `/receive` - Open a gift box and receive stars with animation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

3. Get a bot token from [@BotFather](https://t.me/BotFather) and add it to your `.env` file:
   ```
   BOT_TOKEN=your_actual_bot_token_here
   ```

4. Run the bot:
   ```bash
   python telegram_star.py
   ```

## Recent Fixes

- Updated from aiogram v2 to v3 (latest stable version)
- Fixed compatibility issues with Python 3.13
- Added proper error handling and logging
- Improved animation handling for gift box feature
- Added missing python-dotenv dependency
- Enhanced code structure with try-catch blocks
- Added proper bot initialization validation

## Dependencies

- aiogram==3.15.0 - Telegram Bot API framework
- aiohttp>=3.10.0 - HTTP client/server for asyncio
- python-dotenv>=1.0.0 - Load environment variables from .env file