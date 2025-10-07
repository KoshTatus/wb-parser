import uvicorn
from fastapi import FastAPI, Query
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.dao.dao import ProductDAO
from src.database.database import get_db, create_tables
from src.parser.parser import parse_products_from_wb

app = FastAPI()

@app.get("/products")
def get_products(title = Query(default=""), db: Session = Depends(get_db)):
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

@app.post("/products")
def parse_products(query = Query(default="термопаста"), db: Session = Depends(get_db)):
    result = parse_products_from_wb(query=query)

    ProductDAO.add_products(db, result)

    return {
        "status": "OK",
    }

if __name__ == "__main__":
    create_tables()
    uvicorn.run(app, host="localhost", port=5000)
