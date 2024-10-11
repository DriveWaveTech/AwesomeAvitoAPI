import datetime
import enum
import typing

import pydantic


class ChatTypes(enum.Enum):
    ITEMS = 'u2i'
    USERS = 'u2u'


class Avatar(pydantic.BaseModel):
    default: str
    images: dict


class PublicUserProfile(pydantic.BaseModel):
    avatar: Avatar
    item_id: int
    url: str
    user_id: int


class User(pydantic.BaseModel):
    id: int
    name: str
    public_user_profile: PublicUserProfile


class Link(pydantic.BaseModel):
    text: str
    url: str


class Content(pydantic.BaseModel):
    link: Link


class LastMessage(pydantic.BaseModel):
    author_id: int
    content: Content
    created: datetime.datetime
    direction: str
    id: str
    type: str

    @pydantic.field_validator('created', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)


class Images(pydantic.BaseModel):
    count: int
    main: dict


class Value(pydantic.BaseModel):
    id: int
    images: Images
    price_string: str
    status_id: int
    title: str
    url: str
    user_id: int


class Context(pydantic.BaseModel):
    type: str
    value: Value


class ChatByIdV2Response(pydantic.BaseModel):
    context: Context
    created: datetime.datetime
    id: str
    last_message: LastMessage
    users: typing.List[User]

    @pydantic.field_validator('created', mode='before')
    def validate_created(cls, value: int):  # noqa
        return datetime.datetime.fromtimestamp(value)


class ChatsV2Response(pydantic.BaseModel):
    chats: typing.List[ChatByIdV2Response] = pydantic.Field(default_factory=list)
