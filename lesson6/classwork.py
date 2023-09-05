# Decorators

import time
from typing import Callable

# class Person:
#     # def __init__(self, name: str, age: int) -> None:
#     def init(self, name: str, age: int) -> None:
#         self.name: str = name
#         self.age: int = age


# Person().init()


class Person2:
    pass


def perf_counter(func: Callable):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        exec_time = time.perf_counter() - start
        print(f"Exec time: {func.__name__}: {exec_time}")
        return result

    return inner


class Person:
    _instance = None
    _initialized: bool = False
    _MESSAGE = "Basic error message"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, name: str, age: int) -> None:
        if self._initialized:
            return

        self.name: str = name
        self.age: int = age

        self._initialized = True

    # @classmethod
    @staticmethod
    @perf_counter
    def greeting(name: str):
        print(f"Hello from {name}")

    @property
    def is_adult(self) -> bool:
        if self.age < 18:
            return False
        return True

    @is_adult.setter
    def is_adult(self, value: bool) -> None:
        print("It is not possible override the adult")


john = Person(name="John", age=12)
marry = Person(name="Marry", age=12)

# Person.greeting(john)
# john.greeting()
Person.greeting(name=john.name)
john.greeting(name=john.name)
print(john.is_adult)
john.is_adult = True
# print(Person)
# person.greeting()
