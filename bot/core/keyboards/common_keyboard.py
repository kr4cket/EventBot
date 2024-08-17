from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder


class CommonKeyboard:
    @classmethod
    def get_main_menu_button(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Главное меню', callback_data='/start')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_back_to_main_menu_button(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Вернуться в главное меню', callback_data='/start')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_cancel_registration_button(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Отменить регистрацию', callback_data='/cancel_registration')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_cancel_button(cls) -> InlineKeyboardMarkup:
        key = InlineKeyboardBuilder()

        key.button(text='Отменить действие', callback_data='/cancel')
        key.adjust(1)

        return key.as_markup()

    @classmethod
    def get_cancel_button_data(cls) -> KeyboardBuilder[InlineKeyboardButton]:
        return InlineKeyboardBuilder().button(text='Отменить действие', callback_data='/cancel')

    @classmethod
    def get_main_menu_button_data(cls) -> KeyboardBuilder[InlineKeyboardButton]:
        return InlineKeyboardBuilder().button(text='Главное меню', callback_data='/start')

    @classmethod
    def get_back_to_main_button_data(cls) -> KeyboardBuilder[InlineKeyboardButton]:
        return InlineKeyboardBuilder().button(text='Вернуться в главное меню', callback_data='/start')
