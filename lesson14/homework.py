import asyncio
import logging

import aiohttp

logging.basicConfig(filename="scraper.log", level=logging.INFO)

# Список URL-ов для скрейпинга
urls_to_scrape = [
    "https://www.deepl.com/translator",
    "https://lms.ithillel.ua/",
    "https://www.google.com/search?q=0.04132654+BTC+to+eur&sca_esv=558732412&sxsrf=AM9HkKleW1Wn0ZOXlzEDkuL20ND7moIoSw%3A1696106305082&ei=QYcYZcHNBNnh2roPiZOckAE&ved=0ahUKEwiB8sKumNOBAxXZsFYBHYkJBxIQ4dUDCBA&uact=5&oq=0.04132654+BTC+to+eur&gs_lp=Egxnd3Mtd2l6LXNlcnAiFTAuMDQxMzI2NTQgQlRDIHRvIGV1cjIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwA0iXBVAAWABwAXgBkAEAmAEAoAEAqgEAuAEDyAEA4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp",
]


async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                logging.error(
                    f"Failed to fetch {url}. Status code: {response.status}"
                )
    except aiohttp.ClientError as e:
        logging.error(f"Error fetching {url}: {e}")
    return None


async def save_to_file(data, scrape_data):
    with open(scrape_data, "w", encoding="utf-8") as file:
        file.write(data)


async def scrape_url(url, session):
    data = await fetch_url(session, url)
    if data:
        await save_to_file(data, f'{url.split("/")[-1]}.html')
        logging.info(f"Scraped {url} successfully")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_url(url, session) for url in urls_to_scrape]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
