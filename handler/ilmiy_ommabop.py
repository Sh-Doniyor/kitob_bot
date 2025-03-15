
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.dispatchers import dp
from bot.states import SectorState



@dp.message(SectorState.restoran_menu, F.text == __("Ilmiy ommabop"))
async def meals_handler(message: Message, state: FSMContext) -> None:
    texts = [_("Qiziqarli fizika-Perelman"), _("Tibbiyot mo'jizalari-David Agus"),  _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.meals_menu)
    await message.answer("Ilmiy ommabop", reply_markup=markup)
