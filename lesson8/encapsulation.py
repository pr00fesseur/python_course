from typing import Any


methods_blacklist = [
    "_connect_to_the_atm",
    "_count_the_cash",
    "_get_money",
]


ALLOWED = set()


class PaymentSystem:
    def __init__(self) -> None:
        self.connected_to_the_atm: bool = False

    def __getattribute__(self, name: str) -> Any:
        print(f"Accessing the attribute: {name}")

        if name in methods_blacklist and name not in ALLOWED:
            raise Exception(f"The attribute {name} is private")

        try:
            ALLOWED.remove(name)
        except:
            pass

        return object.__getattribute__(self, name)
        # return super().__getattribute__(name)

    def deposit(self, amount: int):
        pass

    def _connect_to_the_atm(self):
        self.connected_to_the_atm = True
        print("Connected to the ATM")

    def _count_the_cash(self, amount: int):
        print("Counting the cash in the ATM")
        print(f"Total: {amount}")

    # def _PaymentSystem__get_money(self):
    def _get_money(self):
        print("💸 Returning money to the user")

    def withdraw(self, amount: int):
        ALLOWED.add("_connect_to_the_atm")
        ALLOWED.add("_count_the_cash")
        ALLOWED.add("_get_money")

        self._connect_to_the_atm()
        self._count_the_cash(amount)
        self._get_money()


privat = PaymentSystem()
# privat.deposit(amount=100)
privat.withdraw(amount=100)
# privat._PaymentSystem__get_money()
privat._get_money()