
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.db.model import Food
from bot.dispatchers import dp
from bot.states import SectorState


salads = [Food(id=1, name="🥗 caesar salad", image = "AgACAgIAAxkBAAEdZz5nytnHqgAB1OE4f2EiA3qq4keBVw4AAiDnMRt5AVlK6Gokp4D533wBAAMCAAN4AAM2BA", ingredients="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
Food(id=2, name="🥗 olive salad", image="AgACAgIAAxkBAAEdZ0ZnytqGHJ_jPo-aibbGwZ09X07SnwACOOcxG3kBWUrqgWAMcPqlIwEAAwIAA3kAAzYE", ingredients="jkhigytfrydtesrxdcfvgnjk")]



@dp.message(SectorState.restoran_menu, F.text == __("Biznes va rivojlanish"))
async def salad_handler(message: Message, state: FSMContext) -> None:
    texts = [_("Boy ota , kambag'al ota -Robert  Kiyosaki"), _("Muvaffaqiyat odatlari-Stephen Covey"),  _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.salads_menu)
    await message.answer("Biznes va rivojlanish", reply_markup=markup)

