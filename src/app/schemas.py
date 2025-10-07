from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    title: str
    price: int
    rating: float
    review_count: int
    remaining_count: int

class ProductSchema(ProductCreateSchema):
    id: int