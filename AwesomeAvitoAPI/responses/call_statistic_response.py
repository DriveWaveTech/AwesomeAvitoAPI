import typing
from datetime import datetime

from pydantic import BaseModel


class DaysData(BaseModel):
    answered: int
    calls: 0
    new: int
    newAnswered: int
    date: datetime


class CallStatisticResponse(BaseModel):
    itemId: int
    employeeId: int
    days: typing.List[DaysData]

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
