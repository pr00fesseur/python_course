import asyncio
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class UserConfiguration:
    payment_system: str


class PaymentSystem(ABC):
    @abstractmethod
    async def checkout(self, product: Product):
        """Perform the concrete checkout"""

    @abstractmethod
    async def end_connection(self):
        """Close the connection"""


class PayPal(PaymentSystem):
    async def checkout(self, product: Product):
        print("Perform payment with PayPal")

    async def end_connection(self):
        print("Closing connection with PayPal")


class Stripe(PaymentSystem):
    async def checkout(self, product: Product):
        print("Perform payment with Stripe")

    async def end_connection(self):
        print("Closing connection with Stripe")


class PaymentSystemManager:
    def __init__(
        self, authenticated: bool, user_configuration: UserConfiguration
    ) -> None:
        self._authenticated = authenticated
        self._user_configuration = user_configuration
        self._payment_system: PaymentSystem | None = None

    async def __aenter__(self) -> PaymentSystem:
        if self._authenticated is False:
            raise Exception("Please sign in")

        if self._user_configuration.payment_system == "paypal":
            self._payment_system = PayPal()
            return self._payment_system
        elif self._user_configuration.payment_system == "stripe":
            self._payment_system = Stripe()
            return self._payment_system

        raise Exception("Payment system is not supported")

    async def __aexit__(self, *args, **kwargs):
        if self._payment_system:
            await self._payment_system.end_connection()


async def main():
    user_configuration = UserConfiguration(payment_system="stripe")
    phone = Product(id=1, name="phone", price=200)

    async with PaymentSystemManager(
        authenticated=True, user_configuration=user_configuration
    ) as payment_system:
        await payment_system.checkout(phone)


if __name__ == "__main__":
    asyncio.run(main())
