from typing import List
from fastapi import APIRouter, Path

from db import products, database
from models.product import Product, ProductIn

router_product = APIRouter()

# @router_product.get("/fake_products/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = products.insert().values(name=f'product{i+1}',
#                                          description=f'description product {i+1}',
#                                          price=float(i+1))
#         await database.execute(query)
#     return {'message': f'{count} fake products create'}

@router_product.get("/products/", response_model=List[Product])
async def read_products(): 
    query = products.select()
    return await database.fetch_all(query)

@router_product.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int = Path(..., ge=1)):
    query = products.select().where(products.c.productid == product_id)
    return await database.fetch_one(query)

@router_product.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(name=product.name,
                                     description=product.description,
                                     price=product.price)
    last_record = await database.execute(query)
    return last_record

@router_product.put("/products/{product_id}", response_model=Product)
async def update_product(new_product: ProductIn, product_id: int = Path(..., ge=1)):
    query = products.update().where(products.c.productid == product_id).values(productid=product_id,
                                  name = new_product.name,
                                  description=new_product.description,
                                  price = new_product.price)
    record = await database.execute(query)
    return {**new_product.dict(), "id": record}

@router_product.delete("/products/{product_id}")
async def delete_product(product_id: int = Path(..., title="The ID of the product", ge=1)):
    query = products.delete().where(products.c.productid == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}