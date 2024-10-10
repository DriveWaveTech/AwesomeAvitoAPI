import enum
import typing

import pydantic


class ItemStatus(enum.Enum):
    ACTIVE = 'active'
    REMOVED = 'removed'
    OLD = 'old'
    BLOCKED = 'blocked'
    REJECTED = 'rejected'


class Category(pydantic.BaseModel):
    id: int
    name: str


class Meta(pydantic.BaseModel):
    page: int
    per_page: int


class Resource(pydantic.BaseModel):
    id: int
    address: str
    category: Category
    price: int
    status: ItemStatus
    title: str
    url: str


class ItemsInfoResponse(pydantic.BaseModel):
    meta: Meta
    resources: typing.List[Resource]
