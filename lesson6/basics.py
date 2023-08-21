from typing import Callable, Any


def logger(func: Callable) -> Callable:
    def inner(name: str):
        print(f"Running the {func.__name__}...")
        results: Any = func(name)
        if results:
            print(f"Results: {results}")
        else:
            print("There is no results...")

    return inner


@logger
def greeting(name: str) -> None:
    print(f"Hey {name}!")


greeting("John")

# logger(greeting)(name="John")
# logger(greeting, name="John")