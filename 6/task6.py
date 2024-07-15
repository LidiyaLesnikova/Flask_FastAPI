'''
Необходимо создать базу данных для интернет-магазина. База данных должна состоять из 
трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях 
магазина.
• Таблица пользователей должна содержать следующие поля: 
id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: 
id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа 
и статус заказа.
• Таблица товаров должна содержать следующие поля: 
id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для 
каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет"

"Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание.

Критерии оценивания:
1 - Слушатель создал базу данных для интернет-магазина. База данных должна состоять 
из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях 
магазина.
'''

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import starlette.status as status
import uvicorn

from db import database
from routers.user import router_user
from routers.product import router_product
from routers.order import router_order

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def start():
    return RedirectResponse(url="/docs/", status_code=status.HTTP_302_FOUND)

app.include_router(router_user, prefix="/usr")
app.include_router(router_product, prefix="/prod")
app.include_router(router_order, prefix="/ordr")

if __name__ == "__main__":
    uvicorn.run(
        'task6:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )

