def foo():
    print("Hello, I am foo")


def bar(function):
    function.__call__()
    return 12
    # return 13
    # print(f"Hello, {name}")


def baz():
    yield 1
    yield "Hello"
    yield 2
    yield 4
    yield 5


gen = baz()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
