from aiogram.fsm.state import StatesGroup, State


class SectorState(StatesGroup):
    restoran_menu = State()
    salads_menu = State()
    fast_food_menu = State()
    meals_menu = State()
    salad_food = State()
    fast_food = State()
    meal_food = State()
    food_order = State()
    language = State()
