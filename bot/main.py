import asyncio
from bot.core.logger import logger

from aiogram import Dispatcher
from bot.core.common.TelegramBot import TelegramBot
from bot.core.common.HandlerRegistrator import Registrator
from bot.core.common.ServiceRegistrator import ServiceRegistrator

bot = TelegramBot()
dp = Dispatcher()

# Уровень логов
PRODUCTION = 30  # При запуске на Прод
DEBUG = 10  # При разработке

async def main() -> None:
    logger.create(DEBUG)
    Registrator().setup_routers(dp)
    ServiceRegistrator().setup_services()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
