from typing import List

from Project_One.custom_exceptions.incorrect_login import LoginFailed
from Project_One.custom_exceptions.manager_username_does_not_exist import ManagerUsernameDoesNotExistException
from Project_One.dao.manager_dao import ManagerDAO
from Project_One.dao_imp.manager_dao_imp import ManagerDAOImp
from Project_One.entities.manager import Manager
from Project_One.service_dao.manager_service import ManagerServiceDAO


class ManagerServiceImp(ManagerServiceDAO):

    def __init__(self, manager_dao: ManagerDAO):
        self.manager_dao = manager_dao

    # def service_get_manager_information(self, manager_id) -> Manager:
    #     returned_manager = self.manager_dao.get_manager_information(manager_id)
    #     return returned_manager

    def service_get_manager_by_username(self, username: str) -> Manager:
        manager_list = self.manager_dao.get_all_manager_information()
        for existing_manager in manager_list:
            if existing_manager.username == username:
                return self.manager_dao.get_manager_by_username(username)
        raise ManagerUsernameDoesNotExistException("Manager username was not found")

    def service_get_all_manager_information(self) -> list[Manager]:
        all_manager = self.manager_dao.get_all_manager_information()
        return all_manager

    def service_update_manager(self, manager: Manager) -> Manager:
        updated_manager = self.service_update_manager(manager)
        return updated_manager

    def service_check_manager_login(self, manager: Manager) -> Manager:
        for current_manager in self.manager_dao.get_all_manager_information():
            if current_manager.username == manager.username and current_manager.secretword == manager.secretword:
                return self.manager_dao.check_manager_login(manager)
        raise LoginFailed("Login was not successful, please try again.")
