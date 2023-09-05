names: list[str] = ["John", "Marry"]

_names = iter(names)
print(_names.__next__())
print(_names.__next__())
print(_names.__next__())


class Iterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass


instances = Iterator()

for instance in instances:
    print(instance)

while True:
    # name = _names.__next__()
    try:
        value = next(_names)
        print(f"{value=}")
    except StopIteration:
        break
