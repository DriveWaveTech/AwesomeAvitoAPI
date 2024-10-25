import datetime

import pydantic


class Content(pydantic.BaseModel):
    text: str


class PostSendMessageResponse(pydantic.BaseModel):
    content: Content
    created: datetime.datetime
    direction: str
    id: str
    type: str  # TODO: MUST BE ENUM

    @pydantic.field_validator('created', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)
