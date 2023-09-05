def foo():
    # return 1,2,3,4,5
    return (1,)


# data1, data2,data3,data4,data5 = foo()
data = foo()


# print(data)


contact_info = ("John", "Doe", "Kyiv", "33111", "+3801222234", "man", 40)
# name, surname, city, postal_code, phone_number, sex, age = contact_info
name, surname, *meta, age = contact_info

# print(name, surname, age)
# print(meta)


# def create_user(name, surname, city, postal_code, phone_number, sex, age):
def create_user(name, surname, **kwargs):
    print("User is created")
    print(kwargs)
    print(f"The name is {name}")
    print(f"The surname is {surname}")
    # print(f"The city is {city}")


create_user(
    name="John",
    surname="Doe",
    city="Odessa",
    postal_code="33111",
    phone_number="+3801222234",
    sex="man",
    age=40,
)
