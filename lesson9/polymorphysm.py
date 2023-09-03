# print(1 + 1)
# print("1" + "1")

from functools import singledispatch


@singledispatch
def custom_add(a, b):                               #Сначала мы создаем функцию custom_add, которая имеет два аргумента a и b. 
                                                    #Эта функция использует декоратор @singledispatch,
                                                    #который говорит Python, что мы будем регистрировать специальные реализации этой функции для разных типов данных.
    raise NotImplementedError("Unsupported type")

#Затем мы регистрируем две специальные реализации для этой функции
@custom_add.register(int) 
def _(a, b):            #Первая реализация (для типа int)
    return a + b


@custom_add.register(str)
def _(a, b):                #Вторая реализация (для типа str)
    return f"Concat {a}{b}"


print(custom_add(1, 1)) #custom_add(1, 1) вызывает первую реализацию, которая складывает два числа, и результатом будет 2
print(custom_add("1", "1")) #custom_add("1", "1") вызывает вторую реализацию, которая конкатенирует строки, и результатом будет "Concat 11"
print(custom_add(12.2, "1")) #custom_add(12.2, "1") вызывает общее сообщение об ошибке, так как для типа float не была зарегистрирована специальная реализация