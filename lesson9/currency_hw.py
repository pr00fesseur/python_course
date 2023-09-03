

class Price:
    exchange_rates = {
        "USD": {
            "EUR": 0.93,
            "RUB": 96.40,
        },
        "EUR": {
            "USD": 1.10,
            "RUB": 105,
        },
        "RUB": {
            "USD": 0.010,
            "EUR": 0.0095,
        },
    }

    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def convert_to(self, target_currency: str) -> 'Price':
        if self.currency == target_currency:
            return self

        converted_amount = self.amount * Price.exchange_rates[self.currency][target_currency]
        return Price(converted_amount, target_currency)

    def __add__(self, other: 'Price') -> 'Price':
        if self.currency == other.currency:
            new_amount = self.amount + other.amount
            return Price(new_amount, self.currency)
        else:
            new_amount = self.amount + other.convert_to(self.currency).amount
            return Price(new_amount, self.currency)

    def __sub__(self, other: 'Price') -> 'Price':
        if self.currency == other.currency:
            new_amount = self.amount - other.amount
            return Price(new_amount, self.currency)
        else:
            new_amount = self.amount - other.convert_to(self.currency).amount
            return Price(new_amount, self.currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"


# Примеры
price1 = Price(100, "USD")
price2 = Price(50, "EUR")

# Выполнение операций
result_sum = price1 + price2
result_diff = price1 - price2


print("Result of addition:", result_sum)
print("Result of subtraction:", result_diff)



