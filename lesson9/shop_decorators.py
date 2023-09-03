
# def staticmethod(func):
#     def inner(*args, **kwargs):
#         if "self" in args:
#             del from args #неккоректное удаление
#         return func(*args, **kwargs)



class Shop:
    USERS_MAX_SIZE = 300

    def register(self, username, password1, password2, email):
        pass

    def login(self, username, password):
        pass

    @classmethod
    def build_new(cls, domain: str):
        # Host the application on {domain}
        # ...
        cls.USERS_MAX_SIZE
        # cls == Shop
        #Shop.login()
        bershka = Shop()
        zara = Shop()
        return bershka, zara

    @staticmethod
    def get_current_users_amount(user_card_info):
        # number = SELECT COUNT(id) FROM users;
        return 12

    def buy(self, product: dict):
        #self.login(self.user....)
        return None

zara, bershka = Shop.build_new("example.com")




zara.build_new("bershka.com")
Shop.build_new("bershka.com")

zara.buy(
    {
        "pants L": 1222,
    },
)

# Shop.buy(
#     zara,
#     {
#         "pants L": 1222,
#     },
# )

# with staticmethod
# Shop.buy(
#     {
#         "pants L": 1222,
#     },
# )