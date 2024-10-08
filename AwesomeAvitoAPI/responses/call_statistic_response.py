import typing
import datetime

import pydantic


class DaysData(pydantic.BaseModel):
    answered: int
    calls: int
    new: int
    newAnswered: int
    date: datetime.datetime


class CallStatisticResponse(pydantic.BaseModel):
    itemId: int
    employeeId: int
    days: typing.List[DaysData] = pydantic.Field(default_factory=list)

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
