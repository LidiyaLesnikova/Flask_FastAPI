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

from fastapi import FastAPI
import uvicorn

from Tasks import Task

app = FastAPI()
tasks = []

@app.get("/")
async def read_root():
    return "Hello"

@app.get("/tasks/")
async def return_all_tasks():
    return tasks

@app.get("/tasks/{id}")
async def return_task(id: int):
    select = [task for task in tasks if task.id==id]
    if len(select)==1:
        select_task = select[0]
        return {"id": id, "task": select_task}
    else:
        return f"нет Задания с id {id}"

@app.post("/tasks/")
async def create_task(task: Task):
    task = Task(id=len(tasks)+1, title=task.title, description=task.description, status=False)
    tasks.append(task)
    return task

@app.put("/tasks/{id}")
async def update_task(id: int, task: Task):
    select_task = [task for task in tasks if task.id==id]
    if len(select_task)==1:
        index = tasks.index(select_task[0])
        current_task = Task(id=id, title=task.title, description=task.description, status=task.status)
        tasks[index] = current_task
        return current_task
    else:
        return f"нет Задания с id {id}"


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    select_task = [task for task in tasks if task.id==id]
    if len(select_task)==1:
        index = tasks.index(select_task[0])
        tasks.pop(index)
        return f"Задание с id {id} удалено"
    else:
        return f"нет Задания с id {id}"

if __name__ == "__main__":
    uvicorn.run(
        'task5:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
