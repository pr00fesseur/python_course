from typing import Any


class PaymentSystem:
    def __init__(self) -> None:
        self.connected_to_the_atm: bool = False
        self.__deposit = 0

    # getter
    @property
    def deposit(self):
        return self.__deposit

    # setter
    @deposit.setter
    def deposit(self, value: int):
        self.__deposit += value

    # deleter
    @deposit.deleter
    def deposit(self):
        print("Can not delete the object")


privat = PaymentSystem()
print(privat.deposit)
privat.deposit = 12
privat.deposit = 12
print(privat.deposit)


# a = getattr(privat, "depositssss", None)
# setattr(privat, "deposit", 30)

# delattr(privat, "deposit")
# del privat.deposit
