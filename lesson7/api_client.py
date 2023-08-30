from typing import Generic, TypeVar
import requests

# response = requests.get("https://pokeapi.co/api/v2/pokemon/12")
# data = response.json()
# print(f"pokemon is {data['name']}")


# requests.get(...)
# getattr(requests, "get")(...)


class ApiClient:
    ALLOWED_METHODS: list[str] = ["get"]

    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url

    def get_response(self, method: str, endpoint: str) -> dict:
        if method not in self.ALLOWED_METHODS:
            raise NotImplementedError(f"Method {method} is not implemented")

        callback = getattr(requests, method)
        # url = self.base_url + endpoint
        url = "".join([self.base_url, endpoint])
        response = callback(url)

        # response.raise_for_status()

        try:
            return response.json()
        except Exception:
            raise Exception("HTTP request Error")


_ApiClient = TypeVar("_ApiClient", bound=ApiClient)


class ApiClientContext(Generic[_ApiClient]):
    def __init__(self, base_url: str) -> None:
        self._client: _ApiClient | None = None
        self._base_url: str = base_url

    def __enter__(self) -> _ApiClient:
        self._client = ApiClient(base_url=self._base_url)
        self._client.headers = ""
        return self._client

    def __exit__(self, exc_type, exc_value, tb):
        print(f"⚠️ ⚠️ ⚠️ Unexpected client's response: {exc_value}")
        print("Closing the client")
        # self._client.close()

    async def __aenter__(self) -> _ApiClient:
        self._client = ApiClient(base_url=self._base_url)
        self._client.headers = ""
        return self._client

    async def __aexit__(self, exc_type, exc_value, tb):
        print(f"⚠️ ⚠️ ⚠️ Unexpected client's response: {exc_value}")
        print("Closing the client")
        # self._client.close()


# poke_api_client = ApiClient(base_url="https://pokeapi.co/api/v2")
# ditto_data = poke_api_client.get_response(
#     method="get", endpoint="/pokemon/ditto"
# )

# with ApiClientContext[_ApiClient](base_url="https://pokeapi.co/api/v2") as client:
with ApiClientContext(base_url="https://pokeapi.co/api/v2") as client:
    ditto_data = client.get_response(method="get", endpoint="/pokemon/dittoss")
    print(f"Fetched pokemon: {ditto_data['name']}")


async def foo():
    async with ApiClientContext(
        base_url="https://pokeapi.co/api/v2"
    ) as client:
        ditto_data = await client.get_response(
            method="get", endpoint="/pokemon/dittoss"
        )
        print(f"Fetched pokemon: {ditto_data['name']}")
