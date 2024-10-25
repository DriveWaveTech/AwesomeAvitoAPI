import datetime
import typing

import pydantic


class AvailablePrice(pydantic.BaseModel):
    goodness: int
    pricePenny: int


class UserBidsItemResponse(pydantic.BaseModel):
    availablePrices: typing.List[AvailablePrice]
    expirationTime: datetime.datetime
    itemID: int
    pricePenny: int

    @property
    def save_bid(self) -> dict:
        return {
            'expirationTime': self.expirationTime,
            'itemID': self.itemID,
            'pricePenny': self.pricePenny,
        }
