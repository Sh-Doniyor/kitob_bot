
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.dispatchers import dp
from bot.states import SectorState


@dp.message(SectorState.restoran_menu, F.text == __("Badiiy adabiyot"))
async def fast_food_handler(message: Message, state: FSMContext) -> None:
    texts = [_("O'tkan kunlar-Abdulla Qodiriy"), _("Mehrobdan chayon-Cho'pon"),  _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.salads_menu)
    await message.answer("Kitoblar katalogi", reply_markup=markup)

