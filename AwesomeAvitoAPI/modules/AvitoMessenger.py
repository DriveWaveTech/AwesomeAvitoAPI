import pathlib
import typing
import warnings

from AwesomeAvitoAPI.base import AvitoBase

from AwesomeAvitoAPI.responses import PostSendMessageResponse, PostSendImageMessageResponse, ChatsV2Response, \
    ChatTypes, ChatByIdV2Response, MessagesV3Response


class AvitoMessenger(AvitoBase):
    async def post_send_message(
        self,
        chat_id: str,
        message: str,
    ):
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/postSendMessage

        :return:
        """
        if not isinstance(chat_id, str):
            chat_id = str(chat_id)

        if not isinstance(message, str):
            message = str(message)

        response = await self._request(
            method='POST',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v1/accounts/{await self.account_id}/chats/{chat_id}/messages',
            json={
                'message': {
                    'text': message
                },
                'type': 'text'
            }
        )

        return PostSendMessageResponse(**response)

    async def post_send_image_message(
        self,
        chat_id: str,
        image_id: str,
    ) -> PostSendImageMessageResponse:
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/postSendImageMessage

        :return:
        """
        if not isinstance(chat_id, str):
            chat_id = str(chat_id)

        if not isinstance(image_id, str):
            image_id = str(image_id)

        response = await self._request(
            method='POST',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v1/accounts/{await self.account_id}/chats/{chat_id}/messages/image',
            json={
                'image_id': image_id,
            }
        )

        return PostSendImageMessageResponse(**response)

    async def delete_message(
        self,
        chat_id: str,
        message_id: str
    ) -> dict:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/deleteMessage

        :return:
        """
        if not isinstance(chat_id, str):
            chat_id = str(chat_id)

        if not isinstance(message_id, str):
            message_id = str(message_id)

        response = await self._request(
            method='POST',
            headers=await self._auth_header,
            url='https://api.avito.ru/messenger/v1/accounts/'
                f'{await self.account_id}/chats/{chat_id}/messages/{message_id}'
        )

        return response

    async def chat_read(
        self,
        chat_id: str,
    ) -> bool:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/chatRead

        :return:
        """
        if not isinstance(chat_id, str):
            chat_id = str(chat_id)

        response = await self._request(
            method='POST',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v1/accounts/{await self.account_id}/chats/{chat_id}/read'
        )

        return response.get('ok', False)

    async def get_voice_files(
        self,
        *voice_ids: typing.Iterable[str]
    ) -> typing.Dict[str, str]:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/getVoiceFiles

        :return:
        """
        voice_ids = [v for v in voice_ids]

        for i, voice_id in enumerate(voice_ids):
            if not isinstance(voice_id, str):
                voice_ids[i] = str(voice_id)

        response = await self._request(
            method='GET',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v1/accounts/{await self.account_id}/getVoiceFiles',
            params=[
                ('voice_ids', voice_id) for voice_id in voice_ids
            ]
        )

        return response.get('voices_urls', {})

    async def upload_images(
        self,
        *file_paths: typing.Iterable[typing.Union[str, pathlib.Path]],
    ) -> typing.Dict[str, typing.Dict[str, str]]:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/uploadImages

        :return:
        """
        file_paths = [f for f in file_paths]

        for i, file_path in enumerate(file_paths):
            if not isinstance(file_path, str):
                file_paths[i] = str(file_path)

        files = [
            open(file_path, 'rb') for file_path in file_paths  # noqa
        ]

        response = await self._request(
            method='POST',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v1/accounts/{await self.account_id}/uploadImages',
            json={
                'uploadfile': files
            }
        )

        for file in files:
            file.close()

        return response

    async def get_subscriptions(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/getSubscriptions

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def post_webhook_unsubscribe(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/postWebhookUnsubscribe

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def post_blacklist_v2(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/postBlacklistV2

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def get_chats_v2(
        self,
        *item_ids: typing.Iterable[int],
        unread_only: bool = False,
        chat_types: typing.Union[ChatTypes, typing.Iterable[ChatTypes]] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ChatsV2Response:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/getChatsV2

        :return:
        """
        if not isinstance(limit, int):
            limit = 100

        if not isinstance(offset, int):
            offset = 0

        if not chat_types:
            chat_types = [ChatTypes.ITEMS]

        if not isinstance(chat_types, typing.Iterable):
            chat_types = [chat_types]

        params = {
            'limit': 100 if 0 > limit > 100 else limit,
            'offset': offset if offset > 0 else 0,
            'unread_only': unread_only,
            'chat_types': ','.join([chat_type.value for chat_type in chat_types if isinstance(chat_type, ChatTypes)]),
        }

        if item_ids:
            params['item_ids'] = ','.join(str(item_id) for item_id in item_ids if isinstance(item_id, int))

        response = await self._request(
            method='GET',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v2/accounts/{await self.account_id}/chats'
        )

        return ChatsV2Response(**response)

    async def get_all_chats_v2(
        self,
        *item_ids: typing.Iterable[int],
        unread_only: bool = False,
        chat_types: typing.Union[ChatTypes, typing.Iterable[ChatTypes]] = None,
    ) -> typing.AsyncGenerator[ChatsV2Response, None]:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/getChatsV2

        :return:
        """
        offset = 0

        while True:
            chats = await self.get_chats_v2(
                *item_ids,
                unread_only=unread_only,
                chat_types=chat_types,
                limit=100,
                offset=offset,
            )

            yield chats

            if not chats.chats or len(chats.chats) < 100:
                break

            offset += 100

    async def get_chat_by_id_v2(
        self,
        chat_id: typing.Union[int, str],
    ) -> ChatByIdV2Response:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/getChatByIdV2

        :return:
        """
        if not isinstance(chat_id, str):
            chat_id = str(chat_id)

        response = await self._request(
            method='GET',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v2/accounts/{await self.account_id}/chats/{chat_id}'
        )

        return ChatByIdV2Response(**response)

    async def get_messages_v3(
        self,
        chat_id: typing.Union[int, str],
        limit: int = 100,
        offset: int = 0,
    ) -> typing.List[MessagesV3Response]:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/getMessagesV3

        :return:
        """
        if not isinstance(chat_id, str):
            chat_id = str(chat_id)

        if not isinstance(limit, int):
            limit = 100

        if not isinstance(offset, int):
            offset = 0

        response = await self._request(
            method='GET',
            headers=await self._auth_header,
            url=f'https://api.avito.ru/messenger/v3/accounts/{await self.account_id}/chats/{chat_id}/messages/',
            params={
                'limit': 100 if 0 > limit > 100 else limit,
                'offset': offset if offset > 0 else 0,
            }
        )

        return [MessagesV3Response(**r) for r in response]

    async def get_all_messages_v3(
        self,
        chat_id: typing.Union[int, str],
    ) -> typing.AsyncGenerator[typing.List[MessagesV3Response], None]:
        """
        https://developers.avito.ru/api-catalog/messenger/documentation#operation/getMessagesV3

        :return:
        """
        offset = 0

        while True:
            messages = await self.get_messages_v3(
                chat_id=chat_id,
                limit=100,
                offset=offset,
            )

            yield messages

            if not messages or len(messages) < 100:
                break

            offset += 100

    async def post_webhook_v3(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/postWebhookV3

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError
