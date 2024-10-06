from pydantic import BaseModel


class BalanceInfoResponse(BaseModel):
    bonus: int
    real: int

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
