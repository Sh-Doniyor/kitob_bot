from sqlalchemy import select, Text
from sqlalchemy.orm import Mapped, mapped_column

from bot.db import Base
from bot.db.utils import CreatedModel


class Category(CreatedModel):
    __tablename__ = "categories"
    name: Mapped[str]


class Food(CreatedModel):
    name : Mapped[str] = mapped_column(Text)



metadata = Base.metadata