from pprint import pprint as print


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self):
        return f"{self.name} representation"

    def __str__(self) -> str:
        return f"The string representation of {self.name}"

    def another(self):
        return "from another"


john = Person(name="John")

# print("John")
# print(repr("John"))
# print(john.__str__())
# print(john)
# print(str("asdasd"))


# john_has_name, john_has_surname, john_has_age, john_has_city = (
john_contact_info_existence = (
    False,
    True,
    False,
    False,
)

# print(john_contact_info_existence)

# if any(john_contact_info_existence):
#     print("At least one field does exist")

# team = ["John", "Marry", "jack", "Rosa", "Mark"]
# print(sorted(team, reverse=True))
# print(ord("Jis"))
# print(chr(74))

# def ll(argument1, argument2):
#     return argument1 + argument2

# lambda argument1, argument2: argument1 + argument2

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 30, "number": 3},
    {"name": "Cavin", "age": 12, "number": 18},
]


def by_age(item: dict):
    return item["age"]


# print(sorted(team, key=lambda item: item["age"]))


class Animal:
    pass


class Dog(Animal):
    pass


spike = Dog()

# print(isinstance(spike, Animal))
# print(type(spike) == Animal)

john = "John"
marry = "Marry"
# print(john is marry)
# print(type(john) == type(marry))
# print(isinstance(marry, str))
# print(type(marry) == str)


# print(hash("name"))
# print(hash("name"))
# print(hash("name"))


def foo():
    """Some documentation"""

    pass


# print(help(foo))

from itertools import zip_longest

names = ["John", "Marry", "Jack"]
ages = [20, 30, 40, 50]

# for index, name in enumerate(names):
#     print(f"{name=}, age={ages[index]}")

# for name, age in zip(names, ages):
#     print(f"{name=}, {age=}")

for name, age in zip_longest(names, ages):
    print(f"{name=}, {age=}")
