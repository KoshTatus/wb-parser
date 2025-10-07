from sqlalchemy import select
from sqlalchemy.orm import Session

from src.app.schemas import ProductCreateSchema, ProductSchema
from src.database.models import Product


class ProductDAO:
    @classmethod
    def get_all_filtered(cls, db: Session, title: str):
        query = select(Product).where(Product.title.ilike(f"%{title}%"))

        result = db.execute(query).scalars()
        data = [ProductSchema.model_validate(product, from_attributes=True) for product in result]

        return data

    @classmethod
    def add_products(cls, db: Session, products: list[ProductCreateSchema]):
        for product in products:
            new_product = Product(**product.model_dump())
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
