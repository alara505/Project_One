from abc import ABC, abstractmethod
from Project_One.entities.manager import Manager
from typing import List


class ManagerDAO(ABC):

    @abstractmethod
    def get_manager_information(self, manager_id) -> Manager:
        pass

    @abstractmethod
    def get_all_manager_information(self) -> list[Manager]:
        pass

    @abstractmethod
    def update_manager(self, manager: Manager) -> Manager:
        pass

    @abstractmethod
    def check_manager_login(self, manager: Manager) -> Manager:
        pass

