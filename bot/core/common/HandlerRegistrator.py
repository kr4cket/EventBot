from aiogram import Dispatcher

from bot.core.handlers import mainmenu_handler, notify_handler
from bot.core.handlers.registration import user_registration_handler


class Registrator:
    routers = []

    @classmethod
    def register_router(cls, router):
        cls.routers.append(router)

    @classmethod
    def setup_routers(cls, dp: Dispatcher):
        for router in cls.routers:
            dp.include_router(eval(f'{router}.router'))
