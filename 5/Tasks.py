from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: bool #True - выполнена, False - не выполнена
