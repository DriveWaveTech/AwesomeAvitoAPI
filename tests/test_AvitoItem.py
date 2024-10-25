from typing import AsyncGenerator

import pytest
from AwesomeAvitoAPI.responses import ItemsInfoResponse


ignore_test = pytest.mark.skipif("not config.getoption('--all')", reason="Пропускаем этот тест")

@pytest.mark.asyncio
class TestAvitoItem:

    @ignore_test
    async def test_update_price(self, awesome_avito_api):
        ...

    async def test_vas_prices(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.vas_prices()

    @ignore_test #потому как пока не знаю откуда брать item_ids
    async def test_post_calls_stats(self, awesome_avito_api):
        item_ids = 0
        call_stats = await awesome_avito_api.post_calls_stats(item_ids=item_ids)
        assert isinstance(call_stats, list)


    async def test_get_item_info(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.get_item_info()

    async def test_get_items_info(self, awesome_avito_api):
        items = await awesome_avito_api.get_items_info()
        assert isinstance(items, ItemsInfoResponse)
        ...

    async def test_get_all_items_info(self, awesome_avito_api):
        items_generator = await awesome_avito_api.get_all_items_info()
        assert isinstance(items_generator, AsyncGenerator)
        async for item in items_generator:
            assert isinstance(item, ItemsInfoResponse)

    async def test_apply_vas(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.apply_vas()

    async def test_item_stats_shallow(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.item_stats_shallow()
