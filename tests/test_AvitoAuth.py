import pytest


@pytest.mark.asyncio
class TestAvitoAuth:

    async def test_get_access_token(self, awesome_avito_api):
        token = await awesome_avito_api.get_access_token()
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
        print(f"Получен токен: {token}")

    async def test_get_access_token_authorization_code(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.get_access_token_authorization_code()

    async def test_refresh_access_token_authorization_code(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.refresh_access_token_authorization_code()
