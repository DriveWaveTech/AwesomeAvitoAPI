import datetime

import pydantic


class Voice(pydantic.BaseModel):
    voice_id: str


class Location(pydantic.BaseModel):
    kind: str
    lat: float
    lon: float
    text: str
    title: str


class Preview(pydantic.BaseModel):
    description: str
    domain: str
    images: dict
    title: str
    url: str


class Link(pydantic.BaseModel):
    preview: Preview
    text: str
    url: str


class Item(pydantic.BaseModel):
    image_url: str
    item_url: str
    price_string: str
    title: str


class Image(pydantic.BaseModel):
    sizes: dict


class Call(pydantic.BaseModel):
    status: str
    target_user_id: int


class Content(pydantic.BaseModel):
    call: Call
    image: Image
    item: Item
    link: Link
    location: Location
    text: str
    voice: Voice


class Quote(pydantic.BaseModel):
    author_id: str
    content: Content
    created: datetime.datetime
    id: str
    type: str

    @pydantic.field_validator('created', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)


class MessagesV3Response(pydantic.BaseModel):
    author_id: int
    content: Content
    created: datetime.datetime
    direction: str
    id: str
    is_read: bool
    quote: Quote
    read: int
    type: str

    @pydantic.field_validator('created', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)
