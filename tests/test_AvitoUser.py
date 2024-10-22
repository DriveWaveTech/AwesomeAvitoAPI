import pytest
from AwesomeAvitoAPI.responses import UserInfoSelfResponse, UserBalanceResponse


@pytest.mark.asyncio
class TestAvitoUser:
    async def test_get_user_info_self(self, awesome_avito_api):
        user_info = await awesome_avito_api.get_user_info_self()
        assert isinstance(user_info, UserInfoSelfResponse)

        assert isinstance(user_info.id, int)
        assert isinstance(user_info.email, str)
        assert isinstance(user_info.name, str)
        assert isinstance(user_info.phone, int)
        assert isinstance(user_info.profile_url, str)

    async def test_get_user_balance(self, awesome_avito_api):
        user_balance = await awesome_avito_api.get_user_balance()
        assert isinstance(user_balance, UserBalanceResponse)

        assert isinstance(user_balance.bonus, float)
        assert isinstance(user_balance.real, float)


    async def test_post_operations_history(self, awesome_avito_api):
        operations = await awesome_avito_api.post_operations_history()

        assert isinstance(operations, list)
