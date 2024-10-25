import pytest
from AwesomeAvitoAPI.responses import ChatsV2Response, ChatByIdV2Response, MessagesV3Response
from typing import AsyncGenerator

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

    @ignore_test # потому как не знаю какой чат айди брать
    async def test_chat_read(self, awesome_avito_api):
        chat_id = 0
        reader = await awesome_avito_api.chat_read(chat_id=chat_id)
        assert isinstance(reader, bool)

    async def test_get_voice_files(self, awesome_avito_api):
        voice_ids = []
        files = await awesome_avito_api.get_voice_files(voice_ids)
        assert isinstance(files, dict)

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
        item_ids = []
        chats = await awesome_avito_api.get_voice_files(item_ids)
        assert isinstance(chats, ChatsV2Response)

async def test_get_all_chats_v2(self, awesome_avito_api):
        item_ids = []
        chats_generator = await awesome_avito_api.et_all_chats_v2(item_ids)
        assert isinstance(chats_generator, AsyncGenerator)
        async for chat in chats_generator:
            assert isinstance(chat, ChatsV2Response)

    async def test_get_chat_by_id_v2(self, awesome_avito_api):
        chat_id = 0
        chat = await awesome_avito_api.get_voice_files(chat_id)
        assert isinstance(chat, ChatByIdV2Response)

    async def test_get_messages_v3(self, awesome_avito_api):
        chat_id = 0
        messages = await awesome_avito_api.get_messages_v3(chat_id)
        assert isinstance(messages, list)
        for mes in messages:
            assert isinstance(mes, MessagesV3Response)

    async def test_get_all_messages_v3(self, awesome_avito_api):
        chat_id = 0
        messages_generator = await awesome_avito_api.get_all_messages_v3(chat_id)
        assert isinstance(messages_generator, AsyncGenerator)
        async for mes in messages_generator:
            assert isinstance(mes, MessagesV3Response)

    async def test_post_webhook_v3(self, awesome_avito_api):
        with pytest.raises(NotImplementedError):
            await awesome_avito_api.post_webhook_v3()
