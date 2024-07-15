from pydantic import BaseModel, Field

class Product(BaseModel):
    productid: int
    name: str = Field(max_length=32)
    description: str = Field(max_length=100)
    price: float

class ProductIn(BaseModel):
    name: str = Field(max_length=32)
    description: str = Field(max_length=100)
    price: float