from pydantic import BaseModel


class UserInfoResponse(BaseModel):
    id: int
    email: str
    name: str
    phone: int
    profile_url: str

    def __str__(self):
        return f'<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>'
