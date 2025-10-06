from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    title: str
    rating: float
    review_count: int
    remaining_count: int