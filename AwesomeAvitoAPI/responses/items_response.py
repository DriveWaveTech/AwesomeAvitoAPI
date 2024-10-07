import typing

import pydantic

from responses.item_statuses_enum import ItemStatus


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


class ItemsResponse(pydantic.BaseModel):
    meta: Meta
    resources: typing.List[Resource]
