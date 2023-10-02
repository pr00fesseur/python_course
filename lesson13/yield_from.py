from typing import Generator

# def foo():
#     yield 3
#     yield 4
#     yield 5
#     yield 6


# def bar():
#     yield 1
#     yield 2


# def main():
#     yield from foo()
#     yield from bar()


# for i in main():
#     print(i)


def flatten(seq: list[int]) -> Generator[int, None, None]:
    for item in seq:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


data = [1, [2, 3, [4, 5], 6], 7, [8, 9]]

for element in flatten(data):
    print(element)
