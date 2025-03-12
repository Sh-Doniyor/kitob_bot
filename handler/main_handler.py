from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import I18n
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.states import SectorState

main_router = Router()

@main_router.message(SectorState.language, F.text == __("⬅️ Back"))
@main_router.message(SectorState.restoran_menu, F.text == __("⬅️ Back"))
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    texts = [_("🍽 Restoran Menu"), _("📞 Call center"), _("🇺🇿🇬🇧 Lang")]
    markup = build_reply_button(texts, (2,))
    await message.answer(_("🏠 Main Menu:"), reply_markup=markup)


@main_router.message(F.text == __("🇺🇿🇬🇧 Lang"))
async def language_menu_handler(message: Message, state: FSMContext) -> None:
    texts = _("🇺🇿 Uzbek"), _("🇬🇧 English"), _("⬅️ Back")
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.language)
    await message.answer(_("Choose Language: "), reply_markup=markup)


@main_router.message(SectorState.language)
async def language_handler(message: Message, state: FSMContext) -> None:
    print(f"Received message: {message.text}")
    map_lang = {
        "🇺🇿 Uzbek": "uz",
        "🇬🇧 English": "en",
    }
    code = map_lang.get(message.text)
    await state.update_data({"locale": code})
    if hasattr(I18n, "middleware"):
        I18n.middleware.set_locale(code)
    else:
        I18n.current_locale = code
    texts = _("🍽 Restoran Menu"), _("📞 Call center"), _("🇺🇿🇬🇧 Lang")
    markup = build_reply_button(texts, (2,))
    await state.set_state(SectorState.restoran_menu)
    await message.answer(_("🏠 Main Menu:"), reply_markup=markup)


@main_router.message(SectorState.meals_menu, F.text == __("⬅️ Back"))
@main_router.message(SectorState.fast_food_menu, F.text == __("⬅️ Back"))
@main_router.message(SectorState.salads_menu, F.text == __("⬅️ Back"))
@main_router.message(SectorState.food_order, F.text ==  __("⬅️ Back"))
@main_router.message(F.text == __("🍽 Restoran Menu"))
async def restoran_handler(message: Message, state: FSMContext) -> None:
    texts = [_("🥗 Salads"), _("🍕 Fast Food"), _("🍜 Meals"), _("⬅️ Back")]
    markup = build_reply_button(texts, (3, 1))
    await state.set_state(SectorState.restoran_menu)
    await message.answer("🍽 Restoran Menu:", reply_markup=markup)


@main_router.message(F.text == __("📞 Call center"))
async def handle_call_center(message: Message) -> None:
    await message.answer(text="📞 Call Center: +998901234567\n 👩‍💻 @TrendyAdmin")

