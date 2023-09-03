import string
import random

# class Team:
#     def __init__(self, name) -> None:
#         self.name = name
#         self._team = {"John": {}}

#     def __getitem__(self, key: str):
#         if key not in self._team.keys():
#             print("John is not there!!!")
#         else:
#             return self._team[key]


# school_12 = Team(name="School 12")
# school_12["John"]


class User:
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password


class UsersFactory:
    def __init__(self, *args):
        self._names = list(args)
        self._users: dict[str, User] = {}
        self._init_users()

    @property
    def random_password(self):
        return "".join(
            [random.choice(string.ascii_letters) for _ in range(10)]
        )

    def _init_users(self):
        self._users = {
            name.lower(): User(name=name, password=self.random_password)
            for name in self._names
        }

    def __getitem__(self, key: str):
        if key.lower() not in self._users.keys():
            print(f"User {key} is not exist!!!")
        else:
            return self._users[key.lower()]

    def __getattr__(self, name):
        if name not in self._users.keys():
            print(f"User {name} is not exist!!!")
            return None
        else:
            return self._users[name]


users = UsersFactory("John", "Marry")
# print(users["Mark"])
print(users["John"])
print(users.john)