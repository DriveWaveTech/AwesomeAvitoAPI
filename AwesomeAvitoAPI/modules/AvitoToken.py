import asyncio

from AwesomeAvitoAPI.base import AvitoBase
from AwesomeAvitoAPI.responses import TokenResponse


class AvitoToken(AvitoBase):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        loop: asyncio.AbstractEventLoop = None,
        *args,
        **kwargs
    ):
        super().__init__()

        self.loop = loop or asyncio.get_event_loop()

        # Avito Credentials:
        self.client_id: str = client_id
        self.client_secret: str = client_secret

    async def get_access_token(self) -> str:
        """
        Obtaining a temporary token for authorization.

        https://developers.avito.ru/api-catalog/auth/documentation#operation/getAccessToken

        """
        response = await self._request(
            method='POST',
            url="https://api.avito.ru/token/",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
        )

        token_response = TokenResponse(**response)

        self._access_token = token_response.access_token
        self._token_type = token_response.token_type

        return self._access_token
