from abc import ABC, abstractmethod
from Project_One.entities.manager import Manager


class ManagerServiceDAO(ABC):

    # @abstractmethod
    # def service_get_manager_information(self, manager_id) -> Manager:
    #     pass

    @abstractmethod
    def service_get_manager_by_username(self, username: str) -> Manager:
        pass

    @abstractmethod
    def service_get_all_manager_information(self) -> list[Manager]:
        pass

    @abstractmethod
    def service_update_manager(self, manager: Manager) -> Manager:
        pass

    @abstractmethod
    def service_check_manager_login(self, manager: Manager) -> Manager:
        pass
