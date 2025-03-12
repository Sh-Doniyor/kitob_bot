
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


meals = [Food(id=1, name="🍛 Palov", image = "AgACAgIAAxkBAAEdZ2hnyuDTwFsX5tCg8VKP3xzuV9Qa1wACTvMxG9jEUErx4mqR3V-FsgEAAwIAA3kAAzYE", ingredients="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
Food(id=2, name="🍲 Soup", image="AgACAgIAAxkBAAEdZ2pnyuEdzo727YeHD_rOxme-KibwrAACte0xG3sXWUp29n42HBpEHQEAAwIAA3kAAzYE", ingredients="jkhigytfrydtesrxdcfvgnjk")]



@dp.message(SectorState.restoran_menu, F.text == __("🍜 Meals"))
async def meals_handler(message: Message, state: FSMContext) -> None:
    texts = [_("🍛 Palov"), _("🍲 Soup"),  _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.meals_menu)
    await message.answer("🍽 Restoran Menu", reply_markup=markup)


@dp.message(SectorState.meals_menu, F.text == __("🍛 Palov"))
async def meals_menu_handler(message: Message, state: FSMContext) -> None:
    first_meal = meals[0]
    image = first_meal.image
    caption = (f"{_('Name')}: {first_meal.name}\n"
               f"{_('Ingredients')}: {first_meal.ingredients}"
               )
    await state.set_state(SectorState.food_order)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)

@dp.message( F.text == __("🍲 Soup"))
async def meals_menu_handler(message: Message, state: FSMContext) -> None:
    second_meal = meals[1]
    image = second_meal.image
    caption = (f"{_('Name')}: {second_meal.name}\n"
               f"{_('Ingredients')}: {second_meal.ingredients}"
               )
    await state.set_state(SectorState.food_order)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)
