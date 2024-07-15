from datetime import datetime
from typing import List
from fastapi import APIRouter, Path

from db import orders, database
from models.order import Order

router_order = APIRouter()

@router_order.get("/orders/")
async def read_orders(): 
    query = orders.select()
    return await database.fetch_all(query)

@router_order.get("/orders/{order_id}")
async def read_order(order_id: int = Path(..., ge=1)):
    query = orders.select().where(orders.c.orderid == order_id)
    return await database.fetch_one(query)

@router_order.post("/orders/")
async def create_order(order: Order):
    query = orders.insert().values(userid=order.userid,
                                  productid = order.productid, 
                                  create_data=datetime.today(),
                                  status = order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}

@router_order.put("/orders/{order_id}")
async def update_order(new_order: Order, order_id: int = Path(..., ge=1)):
    query = orders.update().where(orders.c.orderid == order_id).values(orderid=order_id, 
                                  userid=new_order.userid,
                                  productid = new_order.productid,
                                  create_data=datetime.today(),
                                  status=new_order.status)
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}

@router_order.delete("/orders/{order_id}")
async def delete_order(order_id: int = Path(..., title="The ID of the order", ge=1)):
    query = orders.delete().where(orders.c.orderid == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}