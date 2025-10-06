from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import Product


class ProductDAO:
    @classmethod
    def get_all_filtered(cls, db: Session, title: str):
        query = select(Product).where(Product.title.ilike(f"%{title}%"))

        result = db.execute(query).all()

        return result