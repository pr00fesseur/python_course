from dataclasses import dataclass
from enum import Enum, StrEnum, auto
from multiprocessing import Process
from threading import Thread
from time import sleep


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


pizza = Dish(
    name="Peperoni",
    size=DishSize.M,
    ingredients=["tomato", "cheese", "peperoni", "dough"],
)

salad = Dish(
    name="Caesar",
    size=DishSize.S,
    ingredients=["tomato", "cheese", "chicken", "dough"],
)


dishes = [pizza, salad]

# regular execution
# for dish in dishes:
#     Kitchen.cook(dish)

# concurrent execution
# threads = [
#     Thread(
#         target=Kitchen.cook,
#         args=(dish,),
#     )
#     for dish in dishes
# ]

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# processes
tasks = [Process(target=Kitchen.cook, args=[dish]) for dish in dishes]

for task in tasks:
    task.start()

for task in tasks:
    task.join()
