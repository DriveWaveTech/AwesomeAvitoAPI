import pytest


ignore_test = pytest.mark.skipif("not config.getoption('--all')", reason="Пропускаем этот тест")

@pytest.mark.asyncio
class TestAvitoMessenger:
    @ignore_test
    async def test_post_send_message(self, awesome_avito_api):
        ...

    @ignore_test
    async def test_post_send_image_message(self, awesome_avito_api):
        ...

    @ignore_test
    async def test_delete_message(self, awesome_avito_api):
        ...

    async def test_chat_read(self, awesome_avito_api):
        ...

    async def test_get_voice_files(self, awesome_avito_api):
        ...

    @ignore_test
    async def test_upload_images(self, awesome_avito_api):
        ...

    async def test_get_subscriptions(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.get_subscriptions()

    async def test_post_webhook_unsubscribe(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.post_webhook_unsubscribe()

    async def test_post_blacklist_v2(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.post_blacklist_v2()

    async def test_get_chats_v2(self, awesome_avito_api):
        ...

    async def test_get_all_chats_v2(self, awesome_avito_api):
        ...

    async def test_get_chat_by_id_v2(self, awesome_avito_api):
        ...

    async def test_get_messages_v3(self, awesome_avito_api):
        ...

    async def test_get_all_messages_v3(self, awesome_avito_api):
        ...

    async def test_post_webhook_v3(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.post_webhook_v3()
