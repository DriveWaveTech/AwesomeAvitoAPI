import pydantic


class BalanceInfoResponse(pydantic.BaseModel):
    bonus: float
    real: float

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
