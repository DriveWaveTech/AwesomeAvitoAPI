import typing
import datetime

import pydantic


class Days(pydantic.BaseModel):
    answered: int
    calls: int
    new: int
    newAnswered: int
    date: datetime.datetime


class PostCallsStatsResponse(pydantic.BaseModel):
    itemId: int
    employeeId: int
    days: typing.List[Days] = pydantic.Field(default_factory=list)

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
