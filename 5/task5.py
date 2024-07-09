'''
Необходимо создать API для управления списком задач. Каждая задача должна содержать 
заглоовок и описание. Для каждой задачи должна быть возможность указать статус 
(выполнена/не выполнена).
API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. 
Для этого использовать библиотеку Pydantic.
'''

import logging
from fastapi import FastAPI
from Tasks import Task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "World"}   

@app.get("/tasks/")
async def return_all_tasks():
    logger.info('Отработал GET запрос.')
    return {"Список ": "World"}   

@app.get("/tasks/{id}")
async def return_task(id: int, task: Task):
    logger.info(f'Отработал PUT запрос для item id = {id}.')
    return {"id": id, "task": task}

@app.post("/tasks/")
async def create_task(task: Task):
    logger.info('Отработал POST запрос.')
    return task

@app.put("/tasks/{id}")
async def update_task(id: int, task: Task):
    logger.info(f'Отработал PUT запрос для item id = {id}.')
    return {"id": id, "task": task}


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    logger.info(f'Отработал DELETE запрос для item id = {id}.')
    return {"id": id}


