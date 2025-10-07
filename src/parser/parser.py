import aiohttp, asyncio

from src.app.schemas import ProductCreateSchema

BASE_URL = "https://search.wb.ru/exactmatch/ru/common/v18/search"

async def get_data(
    params: dict = None,
):
    async with aiohttp.ClientSession() as session:
        response = await session.get(BASE_URL, params=params)
        return await response.json(content_type=None)

async def parse_products_from_wb(query: str):
    params = {
        "appType": 1,
        "query": query,
        "lang": "ru",
        "curr": "rub",
        "dest": "-971646",
        "page": "1",
        "resultset": "catalog",
    }

    try:
        tasks = []
        products = []

        for page in range(1, 51):
            params["page"] = str(page)
            tasks.append(
                asyncio.create_task(
                    get_data(params=params)
                )
            )

        result_list = await asyncio.gather(*tasks)

        for data in result_list:
            for item in data.get("products", []):
                price = item.get("sizes")
                price = price[0]
                price = price["price"]
                price = price.get("basic")
                product = ProductCreateSchema(
                    title=item.get("name"),
                    price=price / 100,
                    rating=item.get("reviewRating", 0),
                    review_count=item.get("feedbacks", 0),
                    remaining_count=item.get("totalQuantity", 0),
                )
                products.append(product)

        return products

    except aiohttp.ClientError as e:
        print(e)