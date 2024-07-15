from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class Status(Enum):
    CREATE = 'Создан'
    HIRED = 'Принят в работу'
    DELIVERY = 'Передан в доставку'
    COMPLETE = 'Исполнен'
    CANCEL = 'Отменен'

class Order(BaseModel):
    userid: int = Field(gt=0)
    productid: int = Field(gt=0)
    status: Status