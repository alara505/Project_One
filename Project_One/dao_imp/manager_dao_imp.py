from Project_One.entities.manager import Manager
from Project_One.dao.manager_dao import ManagerDAO
from Project_One.util.database_connection import connection
from Project_One.custom_exceptions.incorrect_login import LoginFailed


# To make it more robust add update to have employee change their reimbursement after submitting.

class ManagerDAOImp(ManagerDAO):

    # def get_manager_information(self, manager_id) -> Manager:
    #     sql = 'select * from "Project_one".manager where manager_id = %s'
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [manager_id])
    #     manager_record = cursor.fetchone()
    #     manager = Manager(*manager_record)
    #     return manager

    def get_manager_by_username(self, username) -> Manager:
        sql = 'select * from "Project_one".manager where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager

    def get_all_manager_information(self) -> list[Manager]:
        sql = 'select * from "Project_one".manager'
        cursor = connection.cursor()
        cursor.execute(sql)
        manager_records = cursor.fetchall()
        manager_list = []
        for manager in manager_records:
            manager_list.append(Manager(*manager))
        return manager_list

    def update_manager(self, manager: Manager) -> Manager:
        sql = 'update "Project_one".manager set first_name = %s, last_name = %s, username = %s, secretword = %s where manager_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (manager.first_name, manager.last_name, manager.username, manager.secretword, manager.manager_id))
        connection.commit()
        return manager

    def check_manager_login(self, manager: Manager) -> Manager:
        sql = 'select * from "Project_one".manager where username = %s and secretword = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [manager.username, manager.secretword])
        manager_record = cursor.fetchone()
        if manager_record:
            current_manager = Manager(*manager_record)
            return current_manager
        raise LoginFailed("Login was not successful, please try again.")
