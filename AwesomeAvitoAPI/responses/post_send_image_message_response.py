import datetime

import pydantic


class Image(pydantic.BaseModel):
    sizes: dict


class Content(pydantic.BaseModel):
    image: Image


class PostSendImageMessageResponse(pydantic.BaseModel):
    author_id: int
    content: Content
    created: datetime.datetime
    direction: str
    id: str
    type: str

    @pydantic.field_validator('created', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)
