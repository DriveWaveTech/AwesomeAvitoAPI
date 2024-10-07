__all__ = (
    'AwesomeAvitoAPI',
    'AvitoToken',
    'AvitoAdvertisements',
    'AvitoProfile',

    'BalanceInfoResponse',
    'CallStatisticResponse',
    'ItemStatus',
    'ItemsResponse',
    'OperationHistoryResponse',
    'TokenResponse',
    'UserInfoResponse',
)

from modules import *
from responses import *


class AwesomeAvitoAPI(
    AvitoToken,
    AvitoProfile,
    AvitoAdvertisements
):
    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
