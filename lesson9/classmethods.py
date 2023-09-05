import random
import string


class User:
    TOTAL_USERS = 0

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.TOTAL_USERS += 1

    @classmethod
    def create_with_temp_password(cls, username: str):
        temp_chars: list[str] = [
            random.choice(string.ascii_letters) for _ in range(10)
        ]
        temp_password = "".join(temp_chars)
        cls.TOTAL_USERS += 1

        return cls(username=username, password=temp_password)


john = User(username="John", password="12345")
john = User.create_with_temp_password(username="John")
# john = create_user_with_temp_password(username="John")
