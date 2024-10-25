import asyncio
from time import time

from AwesomeAvitoAPI import AwesomeAvitoAPI


async def main():
    avito = AwesomeAvitoAPI(
        client_id='RdKCOkDRlATiZ6Fn6YF0',
        client_secret='DHW-v59T1zTLckeM-NJOKXG3YiJqRkSTyZ_ocnh0',
    )

    print(f'Start GetItems!')
    start = time()

    items_pool = [
        i.id async for items in avito.get_all_items_info() for i in items.resources if items
    ][1:2]

    finish = time()
    print(f'Finish GetItems! ({finish - start})')
    print(items_pool)

    print('= = = = =')

    print(f'Start GetAllChatsV2!')
    start = time()

    chats = set([c async for chat in avito.get_all_chats_v2(*items_pool) for c in chat.chats])

    finish = time()
    print(f'Finish GetAllChatsV2! ({finish - start})')
    print(len(set(chats)))

    await avito._session.close()


asyncio.run(main())
