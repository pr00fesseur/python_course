from dataclasses import dataclass
from enum import StrEnum, auto
from time import sleep



__all__ = ("Kitchen", "Dish", "DishSize")

# import kitchen
# import rest
# rest.Dish
# kitchen.Dish

# from kitchen import Dish as KitchenDish
# from rest import Dish as RestDish

print("I am in kitchen module")

# Bad idea. It runs on import
# import requests
# response = requests.get("google.com")
# response.json()


class DishSize(StrEnum):
    S = auto()
    M = auto()
    L = auto()


@dataclass
class Dish:
    name: str
    size: DishSize
    ingredients: list[str]


class Kitchen:
    @staticmethod
    def heat(dish: Dish):
        """This function is IO-bound task.
        We should wait until meal is warm.
        """

        print(f"\n🕓 Started hitting {dish.name}")
        sleep(3)
        print(f"✅ The {dish} is warm")

    @staticmethod
    def cook(dish: Dish):
        """This function is CPU-bound task.
        We should cook the meal...
        """

        print(f"\n🕓 Started cooking {dish}")
        # NOTE: CPU-bound task
        _ = [i for i in range(150_000_000)]

        print(f"✅ The {dish} is ready")
