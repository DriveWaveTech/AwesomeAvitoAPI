import datetime

import pydantic


class PostOperationHistoryResponse(pydantic.BaseModel):
    amountBonus: int
    amountRub: int
    amountTotal: int
    itemId: int
    operationName: str
    operationType: str
    serviceId: int
    serviceName: str
    serviceType: str
    updatedAt: datetime.datetime

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
