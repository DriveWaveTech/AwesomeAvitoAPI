import pytest
from AwesomeAvitoAPI.responses import ItemsInfoResponse


@pytest.mark.asyncio
class TestAvitoItem:

    @pytest.mark.skip(reason="Пропускаем этот тест")
    async def test_update_price(self, awesome_avito_api):
        ...

    async def test_vas_prices(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.vas_prices()

    @pytest.mark.skip(reason="Пропускаем этот тест")
    async def test_post_calls_stats(self, awesome_avito_api):
        ...

    async def test_get_item_info(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.get_item_info()

    async def test_get_items_info(self, awesome_avito_api):
        items = await awesome_avito_api.get_items_info()
        assert isinstance(items, ItemsInfoResponse)
        ...

    @pytest.mark.skip(reason="Пропускаем этот тест, пока не понял его")
    async def test_get_all_items_info(self, awesome_avito_api):
        ...

    async def test_apply_vas(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.apply_vas()

    async def test_item_stats_shallow(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.item_stats_shallow()
