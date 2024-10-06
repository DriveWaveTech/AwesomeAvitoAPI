import typing
import warnings
from datetime import datetime

from dateutil.relativedelta import relativedelta

from avitoapi.base import AvitoBase
from avitoapi.responses import CallStatisticResponse


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
            data={
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
        date_from: typing.Union[str, datetime] = None,
        date_to: typing.Union[str, datetime] = None,
        item_ids: typing.List[int] = None,
    ):
        """
        https://developers.avito.ru/api-catalog/item/documentation#operation/postCallsStats

        :return:
        """
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
            data={
                'dateFrom': date_from,
                'dateTo': date_to,
                'itemIds': item_ids
            }
        )

        return [CallStatisticResponse(**r) for r in response.get('result', {}).get('items', [])]
