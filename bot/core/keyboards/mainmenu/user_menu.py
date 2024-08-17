from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class UserMainMenu:

    @classmethod
    def get_registration_button(cls) -> ReplyKeyboardMarkup:
        key = ReplyKeyboardBuilder()

        key.button(text='Регистрация', callback_data='/register')
        key.adjust(1)

        return key.as_markup()


    @classmethod
    def get_register_buttons(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Посмотреть мероприятия', callback_data='/get_active_events_list')
        key.button(text='Создать мероприятие', callback_data='/create_event')

        key.adjust(1)

        return key.as_markup()
