import requests

from src.app.schemas import ProductCreateSchema
from src.database.models import Product

BASE_URL = "https://search.wb.ru/exactmatch/ru/common/v18/search"

def get_products(query: str):
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
        products = []

        for page in range(1, 51):
            params["page"] = str(page)
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

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

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []

