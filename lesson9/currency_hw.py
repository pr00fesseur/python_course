

class Price:
    exchange_rates = {"USD": 1.0,
                      "EUR": 0.93,
                      "RUB": 96.40}
    

    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def convert_to_usd(self) -> 'Price':
        if self.currency == "USD":
            return self
        else:
            usd_amount = self.amount / Price.exchange_rates[self.currency]
            return Price(usd_amount, "USD")

    def convert_from_usd(self, target_currency: str) -> 'Price':
        if target_currency == "USD":
            return self
        else:
            target_amount = self.amount * Price.exchange_rates[target_currency]
            return Price(target_amount, target_currency)

    def __add__(self, other: 'Price') -> 'Price':
        if self.currency == other.currency:
            new_amount = self.amount + other.amount
            return Price(new_amount, self.currency)
        else:
            usd_self = self.convert_to_usd()
            usd_other = other.convert_to_usd()
            total_usd = usd_self.amount + usd_other.amount
            return Price(total_usd, "USD")

    def __sub__(self, other: 'Price') -> 'Price':
        if self.currency == other.currency:
            new_amount = self.amount - other.amount
            return Price(new_amount, self.currency)
        else:
            usd_self = self.convert_to_usd()
            usd_other = other.convert_to_usd()
            total_usd = usd_self.amount - usd_other.amount
            return Price(total_usd, "USD")

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"





# Примеры
price1 = Price(300, "USD")
price2 = Price(70, "RUB")

# Выполнение операций
result_sum = price1 + price2
result_diff = price1 - price2


print("Result of addition:", result_sum)
print("Result of subtraction:", result_diff)



