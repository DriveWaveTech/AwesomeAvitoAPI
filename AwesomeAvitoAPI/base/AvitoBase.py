import asyncio
import typing

import aiohttp

from AwesomeAvitoAPI.base.Logger import Logger
from AwesomeAvitoAPI.base.exceptions import AvitoAPIServiceError, AvitoAPIServiceUnavailableError, \
    AvitoAPIWrongResponseError, AvitoAPINotImplementedError
from AwesomeAvitoAPI.responses import TokenType


class AvitoBase(Logger):
    MAX_TRIES = 3
    SLEEP_TIME = 1.5

    def __init__(self):
        super().__init__()

        self._session = aiohttp.ClientSession()

        # General Attributes:
        self.loop: typing.Optional[asyncio.AbstractEventLoop] = None
        self._account_id: typing.Optional[int] = None
        self._access_token: typing.Optional[str] = None
        self._token_type: typing.Optional[TokenType] = None

    async def _request(self, method: str, url: str, **kwargs) -> typing.Optional[dict]:
        execute = {
            'GET': self._session.get,
            'POST': self._session.post,
            # (Using only GET and POST methods)
        }.get(method.upper(), self._session.get)

        tries = 0
        is_expired = False

        while tries < AvitoBase.MAX_TRIES:
            async with execute(url=url, **kwargs) as response:
                match response.status:
                    case 200:
                        if not (_json := await response.json()).get('error'):
                            return _json

                        self._warn(f'Wrong response answer: {_json}')

                    case 401 | 403:
                        self._warn(f'Wrong response status! ({response.status})')
                        await asyncio.sleep(self.SLEEP_TIME)

                        if not is_expired:
                            is_expired = True
                            await self.get_access_token()
                            continue

                    case 429:
                        self._warn(f'Too many requests! ({response.status})')
                        await asyncio.sleep(self.SLEEP_TIME * 2)
                        continue

                    case 500:
                        raise AvitoAPIServiceError

                    case 503:
                        raise AvitoAPIServiceUnavailableError

                    case _:
                        self._warn(f'Wrong response status! ({response.status})')
                        await asyncio.sleep(self.SLEEP_TIME)

            tries += 1

        raise AvitoAPIWrongResponseError

    async def get_access_token(self):
        raise AvitoAPINotImplementedError

    async def get_info(self):
        raise AvitoAPINotImplementedError

    @property
    async def account_id(self) -> int:
        if not self._account_id:
            await self.get_info()

        return self._account_id

    @property
    async def access_token(self):
        if not self._access_token:
            await self.get_access_token()

        return self._access_token

    @property
    async def token_type(self):
        if not self._token_type:
            await self.get_access_token()

        return self._token_type

    @property
    async def _auth_header(self):
        if not await self.access_token:
            raise AvitoAPINotImplementedError

        if not await self.token_type:
            raise AvitoAPINotImplementedError

        return {'Authorization': f'{self._token_type.value} {self._access_token}'}
