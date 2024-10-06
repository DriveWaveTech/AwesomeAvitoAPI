import asyncio

from AvitoAPI import AvitoAPI


async def main():
    avito = AvitoAPI(
        client_id="TEST",
        client_secret="TEST",
    )

    print(await avito.get_info())

    await asyncio.Event().wait()


asyncio.run(main())