
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.inline import pagination_inline_button
from bot.buttons.reply import build_reply_button
from bot.dispatchers import dp
from bot.states import SectorState
from db.model import Food


fast_food = [Food(id=1, name="🍔 Burger", image = "AgACAgIAAxkBAAEdbFJnzUpHsgLRzgABG1nAiUe3vigbnYQAApzlMRvHS3BKgPqnEH6_EQgBAAMCAANtAAM2BA", ingredients="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
Food(id=2, name="🌭 Hot-dog", image="AgACAgIAAxkBAAEdZ2Jnyt9e9-55RuWUE_Hjj3jdlN9zYAACS_MxG9jEUEotxq-WcxTj8gEAAwIAA3kAAzYE", ingredients="jkhigytfrydtesrxdcfvgnjk")]


@dp.message(SectorState.restoran_menu, F.text == __("🍕 Fast Food"))
async def fast_food_handler(message: Message, state: FSMContext) -> None:
    texts = [_("🍔 Burger"), _("🌭 Hot-dog"),  _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.salads_menu)
    await message.answer("🍽 Restoran Menu", reply_markup=markup)


@dp.message(SectorState.fast_food_menu, F.text == __("🍔 Burger"))
async def fast_food_menu_handler(message: Message, state: FSMContext) -> None:
    first_food = fast_food[0]
    image = first_food.image
    caption = (f"{_('Name')}: {first_food.name}\n"
               f"{_('Ingredients')}: {first_food.ingredients}"
               )
    await state.set_state(SectorState.food_order)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)

@dp.message( F.text == __("🌭 Hot-dog"))
async def fast_food_menu_handler(message: Message, state: FSMContext) -> None:
    second_food = fast_food[1]
    image = second_food.image
    caption = (f"{_('Name')}: {second_food.name}\n"
               f"{_('Ingredients')}: {second_food.ingredients}"
               )
    await state.set_state(SectorState.food_order)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)
