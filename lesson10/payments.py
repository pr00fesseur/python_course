from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: int):
        pass

    @abstractmethod
    def display_payment(self):
        pass

    def apply_discount(self, amount: int, percentage: int):
        discount = (percentage / 100) * amount
        return int(amount - discount)


class CreditCard(PaymentStrategy):
    def process_payment(self, amount: int):
        amount = self.apply_discount(amount, 5)

        print(f"Processing credit card payment of ${amount}")

    def display_payment(self):
        print("Credit crad payment")


def payment_processor(strategy: PaymentStrategy):
    strategy.process_payment(100)
    print("Payment processor is Done")


payment_processor(strategy=CreditCard())
