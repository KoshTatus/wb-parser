from fastapi import FastAPI, Query
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.app.dao import ProductDAO
from src.database.database import get_db

app = FastAPI()


@app.get("/products")
def get_products(title = Query(), db: Session = Depends(get_db)):
    result = ProductDAO.get_all_filtered(db, title)

    return {
        "data" : [
            {
                "id": product.id,
                "title": product.title,
                "rating": product.rating,
                "reviewCount": product.review_count,
                "remainingCount": product.remaining_count,
            }
            for product in result
        ]
    }
