import string
from random import randint, choice
from dataclasses import dataclass

from typing import Generator


@dataclass
class User:
    id: int
    name: str


def _random_user() -> Generator[User, None, None]:
    """Create a unique random user."""

    users_ids: set[int] = set()

    while True:
        random_user = User(
            id=randint(1, 1000),
            name="".join(
                [choice(string.ascii_letters) for _ in range(randint(5, 10))]
            ),
        )

        if random_user.id in users_ids:
            continue

        users_ids.add(random_user.id)
        yield random_user


random_user = _random_user()
