import warnings

from AwesomeAvitoAPI.base import AvitoBase


class AvitoAccountsHierarchy(AvitoBase):
    async def check_ah_user_v1(self):
        """
        TODO: https://developers.avito.ru/api-catalog/accounts-hierarchy/documentation#operation/checkAhUserV1

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def get_employees_v1(self):
        """
        TODO: https://developers.avito.ru/api-catalog/accounts-hierarchy/documentation#operation/getEmployeesV1

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def link_items_v1(self):
        """
        TODO: https://developers.avito.ru/api-catalog/accounts-hierarchy/documentation#operation/linkItemsV1

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError

    async def list_items_by_employee_id_v1(self):
        """
        TODO: https://developers.avito.ru/api-catalog/accounts-hierarchy/documentation#operation/listItemsByEmployeeIdV1

        :return:
        """
        warnings.warn(f'This method still in development and deprecated!', PendingDeprecationWarning)
        raise NotImplementedError
