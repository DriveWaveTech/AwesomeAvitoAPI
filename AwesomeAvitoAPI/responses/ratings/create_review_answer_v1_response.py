import datetime

import pydantic


class CreateReviewAnswerV1(pydantic.BaseModel):
    id: int
    createdAt: datetime.datetime

    @pydantic.field_validator('createdAt', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)
