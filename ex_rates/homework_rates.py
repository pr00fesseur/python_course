import argparse
import asyncio

import httpx
from pydantic import BaseModel, Field

API_KEY = "SKUAXIROMN3FQWSR"
BASE_URL = "https://www.alphavantage.co"


class AlphavantageCurrencyExchangeRatesRequest(BaseModel):
    currency_from: str
    currency_to: str


class AlphavantageCurrencyExchangeRatesResults(BaseModel):
    currency_from: str = Field(alias="1. From_Currency Code")
    currency_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")


class AlphavantageCurrencyExchangeRatesResponse(BaseModel):
    results: AlphavantageCurrencyExchangeRatesResults = Field(
        alias="Realtime Currency Exchange Rate"
    )


async def fetch_currency_exchange_rate(
    session, currency_from, currency_to, api_key
):
    payload = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": currency_from.upper(),
        "to_currency": currency_to.upper(),
        "apikey": api_key,
    }
    async with session.get(BASE_URL + "/query", params=payload) as response:
        data = await response.json()
        exchange_rate = data.get("Realtime Currency Exchange Rate", {}).get(
            "5. Exchange Rate"
        )
        return f"{currency_from} to {currency_to}: {exchange_rate}"


async def main():
    parser = argparse.ArgumentParser(
        prog="Currency exchange rates fetcher",
        description="This app fetches exchange rates from Alphavantage",
    )
    parser.add_argument(
        "source_currencies", nargs="+", help="Source currencies"
    )
    parser.add_argument("--target", help="Target currency")

    args = parser.parse_args()

    target_currency = args.target.upper()
    source_currencies = [
        currency.upper() for currency in args.source_currencies
    ]

    async with httpx.AsyncClient() as session:
        tasks = [
            fetch_currency_exchange_rate(
                session, source_currency, target_currency, API_KEY
            )
            for source_currency in source_currencies
        ]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
