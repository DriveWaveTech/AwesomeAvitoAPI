import typing
import warnings

from AwesomeAvitoAPI.base import AvitoBase

from AwesomeAvitoAPI.responses import PostSendMessageResponse, PostSendImageMessageResponse


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
        if not isinstance(voice_ids, list):
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

    async def upload_images(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/uploadImages

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

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

    async def get_chats_v2(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/getChatsV2

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def get_chat_by_id_v2(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/getChatByIdV2

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def get_messages_v3(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/getMessagesV3

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def post_webhook_v3(self):
        """
        TODO: https://developers.avito.ru/api-catalog/messenger/documentation#operation/postWebhookV3

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError
