
from handler import fast_food_handler
from handler import main_handler
from handler import meals_handler
from handler import salads_handler

from bot.dispatchers import dp
from handler.main_handler import main_router
dp.include_routers(main_router)

