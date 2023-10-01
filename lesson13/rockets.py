import random
import time
from threading import Thread
from typing import Generator

Rocket = tuple[str, float, int]


def random_delay() -> float:
    # [ 0.0 .. 5.0 )
    return random.random() * 5


def random_countdown() -> int:
    return random.randrange(5)


def launch_rocket(*_, rocket_name: str, delay: float, countdown: int):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i+1}...")
        time.sleep(1)
    print(f"Rocket {rocket_name} is launched")


def create_rockets(n: int = 10_000) -> Generator[Rocket, None, None]:
    for i in range(1, n + 1):
        yield f"AA-{i}", random_delay(), random_countdown()


def run():
    # rockets = [
    #     ("AA-12", random_delay(), random_countdown()),
    #     ("BB-12", random_delay(), random_countdown()),
    #     ("CC-12", random_delay(), random_countdown()),
    # ]

    rockets: Generator[Rocket, None, None] = create_rockets()

    # Using threads
    threads: list[Thread] = [
        Thread(
            target=launch_rocket,
            kwargs={
                "rocket_name": name,
                "delay": delay,
                "countdown": countdown,
            },
        )
        for name, delay, countdown in rockets
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("All rockets are successfully launched!!!")

    # Sync
    # for name, delay, countdown in rockets:
    #     launch_rocket(
    #         rocket_name=name,
    #         delay=delay,
    #         countdown=countdown,
    #     )


if __name__ == "__main__":
    run()
