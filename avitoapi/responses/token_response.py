from enum import Enum

from pydantic import BaseModel


class TokenType(Enum):
    BEARER = 'Bearer'


class TokenResponse(BaseModel):
    access_token: str
    expires_in: int
    token_type: TokenType

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
