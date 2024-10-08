import typing
import warnings
from datetime import datetime

from dateutil.relativedelta import relativedelta

from AwesomeAvitoAPI.base import AvitoBase
from AwesomeAvitoAPI.responses import CallStatisticResponse, ItemStatus, ItemsResponse


class AvitoAdvertisements(AvitoBase):
    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__()

    async def update_ad_price(self, item_id: int, price: int) -> bool:
        """
        https://developers.avito.ru/api-catalog/item/documentation#operation/updatePrice

        :param item_id:
        :param price:
        :return:
        """
        if not isinstance(price, int):
            raise ValueError("Price must be an integer")

        if not isinstance(item_id, int):
            raise ValueError("Item ID must be an integer")

        headers = await self._auth_header
        headers['Content-Type'] = 'application/json'

        response = await self._request(
            method='POST',
            url=f'https://api.avito.ru/core/v1/items/{item_id}/update_price',
            headers=headers,
            json={
                'price': price
            }
        )

        return response.get('result', {}).get('success', False)

    async def get_cost_of_services(self):
        """
        https://developers.avito.ru/api-catalog/item/documentation#operation/vasPrices

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def get_call_statistics(
        self,
        item_ids: typing.Union[int, typing.List[int]],
        date_from: typing.Union[str, datetime] = None,
        date_to: typing.Union[str, datetime] = None,
    ):
        """
        https://developers.avito.ru/api-catalog/item/documentation#operation/postCallsStats

        :return:
        """
        if isinstance(item_ids, int):
            item_ids = [item_ids]

        for i in item_ids:
            if not isinstance(i, int):
                raise ValueError("Item ID must be an integer")

        if not date_to:
            date_to = datetime.now()

        if not date_from:
            date_from = date_to - relativedelta(years=1)

        if isinstance(date_from, datetime):
            date_from = date_from.strftime("%Y-%m-%d")

        if isinstance(date_to, datetime):
            date_to = date_to.strftime("%Y-%m-%d")

        headers = await self._auth_header
        headers['Content-Type'] = 'application/json'

        response = await self._request(
            method='POST',
            url=f'https://api.avito.ru/core/v1/accounts/{await self.account_id}/calls/stats/',
            headers=headers,
            json={
                'dateFrom': date_from,
                'dateTo': date_to,
                'itemIds': item_ids
            }
        )

        return [CallStatisticResponse(**r) for r in response.get('result', {}).get('items', [])]

    async def get_items(
        self,
        per_page: int = 25,
        page: int = 1,
        updated_at_from: typing.Union[str, datetime] = None,
        category: typing.Optional[int] = None,
        *statuses: typing.Tuple[ItemStatus]
    ):
        """
        https://developers.avito.ru/api-catalog/item/documentation#operation/getItemsInfo

        :return:
        """
        for status in statuses:
            if not isinstance(status, ItemStatus):
                raise ValueError("Status must be an instance of ItemStatus")

        params = {
            'per_page': per_page,
            'page': page,
        }

        if isinstance(updated_at_from, datetime):
            updated_at_from = updated_at_from.strftime("%Y-%m-%d")

        if updated_at_from:
            params['updatedAtFrom'] = updated_at_from

        if category:
            params['category'] = category

        if statuses:
            params['status'] = ','.join([s.value for s in statuses])  # noqa

        headers = await self._auth_header
        headers['Content-Type'] = 'application/json'

        response = await self._request(
            method='GET',
            url='https://api.avito.ru/core/v1/items',
            headers=headers,
            params=params
        )

        return ItemsResponse(**response)

    async def get_all_items(self):
        """
        https://developers.avito.ru/api-catalog/item/documentation#operation/getItemsInfo

        :return:
        """
        page = 1

        while True:
            items = await self.get_items(per_page=100, page=page)

            yield items

            if not items or len(items.resources) < 100:
                break

            page += 1
