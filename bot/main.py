import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.utils.i18n import FSMI18nMiddleware, I18n

from bot.dispatchers import TOKEN
from handler import *


async def main() -> None:
    i18n = I18n(path="../locales")
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
