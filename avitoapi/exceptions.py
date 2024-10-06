__all__ = (
    'AvitoAPIBaseException',
    'AvitoAPIWrongResponseError',
    'AvitoAPINotImplementedError',
    'AvitoAPIServiceUnavailableError',
    'AvitoAPIServiceError'
)


class AvitoAPIBaseException(Exception):
    """ Base level exceptions raised errors. """


class AvitoAPIWrongResponseError(AvitoAPIBaseException):
    def __init__(self):
        super().__init__('Failed to get response from API!')


class AvitoAPINotImplementedError(AvitoAPIBaseException):
    def __init__(self):
        super().__init__('This class object could not be using outside of AvitoAPI tool!')


class AvitoAPIServiceUnavailableError(AvitoAPIBaseException):
    def __init__(self):
        super().__init__('Avito API service temporarily unavailable. Please, contact to Avito support!')


class AvitoAPIServiceError(AvitoAPIBaseException):
    def __init__(self):
        super().__init__('Error while processing request. Please, contact to Avito support!')
