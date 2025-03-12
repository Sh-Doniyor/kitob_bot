from dataclasses import dataclass


class CRUD:
    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def get(self):
        pass


@dataclass
class Category(CRUD):
    id: int = None
    name: str = None
    parent_id: int = None

@dataclass
class Food(CRUD):
    id: int = None
    image: str = None
    name: str = None
    ingredients: str = None