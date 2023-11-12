from data import config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

# Dispatcher 
dp = Dispatcher()

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(config.Token, parse_mode=ParseMode.HTML)
    # Import all dispatchers
    from handlers import dp
    # And the run events dispatching
    await dp.start_polling(bot)