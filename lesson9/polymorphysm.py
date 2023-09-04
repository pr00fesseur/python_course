# print(1 + 1)
# print("1" + "1")

from functools import singledispatch


@singledispatch
def custom_add(a, b):
    raise NotImplementedError("Unsupported type")


# Затем мы регистрируем две специальные реализации для этой функции
@custom_add.register(int)
def _(a, b):  # Первая реализация (для типа int)
    return a + b


@custom_add.register(str)
def _(a, b):  # Вторая реализация (для типа str)
    return f"Concat {a} {b}"


print(custom_add(1, 1))

print(custom_add("1", "1"))

print(custom_add(12.2, "1"))
