import typing
from datetime import datetime

from dateutil.relativedelta import relativedelta

from base import AvitoBase
from responses import UserInfoResponse, BalanceInfoResponse, OperationHistoryResponse


class AvitoProfile(AvitoBase):
    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__()

    async def get_info(self) -> UserInfoResponse:
        """
        https://developers.avito.ru/api-catalog/user/documentation#operation/getUserInfoSelf

        :return:
        """
        response = await self._request(
            method="GET",
            url="https://api.avito.ru/core/v1/accounts/self",
            headers=await self._auth_header
        )

        user_info_response = UserInfoResponse(**response)

        if not self._account_id:
            self._account_id = user_info_response.id

        return user_info_response

    async def get_balance(self) -> BalanceInfoResponse:
        """
        https://developers.avito.ru/api-catalog/user/documentation#operation/getUserBalance

        :return:
        """
        response = await self._request(
            method="GET",
            url=f"https://api.avito.ru/core/v1/accounts/{await self.account_id}/balance/",
            headers=await self._auth_header
        )

        return BalanceInfoResponse(**response)

    async def get_operation_history(
        self,
        datetime_from: typing.Union[str, datetime] = None,
        datetime_to: typing.Union[str, datetime] = None,
    ) -> typing.Optional[typing.List[OperationHistoryResponse]]:
        """
        https://developers.avito.ru/api-catalog/user/documentation#operation/postOperationsHistory

        :param datetime_from:
        :param datetime_to:
        :return:
        """
        if not datetime_to:
            datetime_to = datetime.now()

        if not datetime_from:
            datetime_from = datetime_to - relativedelta(years=1)

        if isinstance(datetime_from, datetime):
            datetime_from = datetime_from.strftime("%Y-%m-%d")

        if isinstance(datetime_to, datetime):
            datetime_to = datetime_to.strftime("%Y-%m-%d")

        headers = await self._auth_header
        headers["Content-Type"] = "application/json"

        response = await self._request(
            method="POST",
            url="https://api.avito.ru/core/v1/accounts/operations_history/",
            headers=headers,
            data={
                'dateTimeFrom': datetime_from,
                'dateTimeTo': datetime_to,
            }
        )

        return [OperationHistoryResponse(**r) for r in response]
