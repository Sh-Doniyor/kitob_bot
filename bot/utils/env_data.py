from os import getenv
from bot.utils.settings import ENV_PATH
from dotenv import load_dotenv
load_dotenv(ENV_PATH)

class BotConfig:
    TOKEN = getenv("BOT_TOKEN")

class DBConfig:
    DB_NAME = getenv("DB_NAME")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")
    DB_PORT = getenv("DB_PORT")
    DB_URL = getenv("DB_ASYNC_URL")

class WebConfig:
    ADMIN_USERNAME = getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD")
class Config:
    bot = BotConfig()
    db = DBConfig()
    web = WebConfig()
