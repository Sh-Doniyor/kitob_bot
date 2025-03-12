from aiogram.types import  InlineKeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


def pagination_inline_button():
    ikb = InlineKeyboardBuilder()
    ikb.add(*[InlineKeyboardButton(text = _("Order"), callback_data="order")])
    ikb.adjust(3, 3)
    return ikb.as_markup()