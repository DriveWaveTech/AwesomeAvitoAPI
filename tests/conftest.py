import pytest
from AwesomeAvitoAPI.modules import AwesomeAvitoAPI

#  Made in UZB
@pytest.fixture(scope="session")
async def awesome_avito_api():
    """Фикстура для создания единственного экземпляра AwesomeAvitoAPI на весь тестовый прогон"""
    avito_api = AwesomeAvitoAPI(client_id="",
                                client_secret="")
    yield avito_api
    await avito_api._session.close()
