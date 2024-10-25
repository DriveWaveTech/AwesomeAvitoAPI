import typing

from AwesomeAvitoAPI.base import AvitoBase

from AwesomeAvitoAPI.responses import UserBidsItemResponse


class AvitoAuction(AvitoBase):
    async def get_user_bids(
        self,
        from_item_id: int = 0,
        batch_size: int = 200
    ) -> typing.List[UserBidsItemResponse]:
        """
        https://developers.avito.ru/api-catalog/auction/documentation#operation/getUserBids

        :return:
        """
        if not isinstance(from_item_id, int):
            raise ValueError('from_item_id must be an integer')

        if not isinstance(batch_size, int):
            raise ValueError('batch_size must be an integer')

        response = await self._request(
            method='GET',
            url='https://api.avito.ru/auction/1/bids',
            params={
                'fromItemID': from_item_id if from_item_id > 0 else 0,
                'batchSize': batch_size if 200 > batch_size > 0 else 200,
            }
        )

        return [UserBidsItemResponse(**r) for r in response.get('items', [])]

    async def save_item_bids(
        self,
        items: typing.List[UserBidsItemResponse],
    ) -> bool:
        """
        https://developers.avito.ru/api-catalog/auction/documentation#operation/saveItemBids

        :return:
        """
        for item in items:
            if not isinstance(item, (UserBidsItemResponse, dict)):
                raise ValueError('items must be an instance of UserBidsItemResponse or dict')

            if isinstance(item, dict):
                if len(item) == 2 and any(key not in item for key in ['pricePenny', 'itemID']):
                    raise ValueError('item dict must contains pricePenny and itemID values!')

                elif len(item) == 3 and any(key not in item for key in ['pricePenny', 'itemID', 'expirationTime']):
                    raise ValueError('item dict must contains pricePenny, itemID and expirationTime values!')

                else:
                    raise ValueError('item dict must contains pricePenny, itemID and expirationTime values!')

        await self._request(
            method='POST',
            url='https://api.avito.ru/auction/1/bids',
            json={
                'items': [
                    (item.save_bid if isinstance(item, UserBidsItemResponse) else item)
                    for item in items
                ],
            }
        )

        return True
