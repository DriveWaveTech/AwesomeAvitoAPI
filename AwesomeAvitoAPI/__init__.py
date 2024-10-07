__all__ = (
    'AwesomeAvitoAPI',
)

from modules.AvitoAdvertisements import AvitoAdvertisements
from modules.AvitoProfile import AvitoProfile
from modules.AvitoToken import AvitoToken


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
