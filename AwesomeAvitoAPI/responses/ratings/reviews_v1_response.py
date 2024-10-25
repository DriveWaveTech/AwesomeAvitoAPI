import datetime
import typing

import pydantic


class Sender(pydantic.BaseModel):
    name: str


class Item(pydantic.BaseModel):
    id: int
    title: str


class Size(pydantic.BaseModel):
    size: str
    url: str


class Image(pydantic.BaseModel):
    number: int
    sizes: typing.List[Size]


class ExtraParams(pydantic.BaseModel):
    vin: str


class RejectReasons(pydantic.BaseModel):
    id: int
    title: str


class Answer(pydantic.BaseModel):
    id: int
    createdAt: datetime.datetime
    reject_reasons: typing.List[RejectReasons]
    status: str
    text: str

    @pydantic.field_validator('createdAt', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)


class Reviews(pydantic.BaseModel):
    id: int
    answer: Answer
    canAnswer: bool
    createdAt: datetime.datetime
    extraParams: ExtraParams
    images: typing.List[Image]
    item: Item
    score: int
    sender: Sender
    stage: str
    text: str
    usedInScore: bool

    @pydantic.field_validator('createdAt', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)


class ReviewsV1Response(pydantic.BaseModel):
    reviews: typing.List[Reviews]
    total: int
