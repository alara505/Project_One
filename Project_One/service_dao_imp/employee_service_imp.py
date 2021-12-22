from typing import List
from Project_One.custom_exceptions.incorrect_information import IncorrectCredentials
from Project_One.custom_exceptions.incorrect_login import LoginFailed
from Project_One.custom_exceptions.employee_username_does_not_exist import EmployeeUsernameDoesNotExistException
from Project_One.dao.employee_dao import EmployeeDAO
from Project_One.dao_imp.employee_dao_imp import EmployeeDAOImp
from Project_One.entities.employees import Employee
from Project_One.service_dao.employee_service import EmployeeServiceDAO


class EmployeeServiceImp(EmployeeServiceDAO):

    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    # def service_get_employee_information(self, employee_id: int) -> Employee:
    #     returned_employee = self.employee_dao.get_employee_information(employee_id)
    #     return returned_employee

    def service_get_employee_by_username(self, username: str) -> Employee:
        employee_list = self.employee_dao.get_all_employee_information()
        for existing_employee in employee_list:
            if existing_employee.username == username:
                return self.employee_dao.get_employee_by_username(username)
        raise EmployeeUsernameDoesNotExistException("Employee username was not found")

    def service_get_all_employee_information(self) -> list[Employee]:
        all_employee = self.employee_dao.get_all_employee_information()
        return all_employee

    def update_employee(self, employee: Employee) -> Employee:
        updated_employee = self.update_employee(employee)
        return updated_employee

    def service_check_employee_login(self, employee: Employee) -> Employee:
        for current_employee in self.employee_dao.get_all_employee_information():
            if current_employee.username == employee.username and current_employee.secretword == employee.secretword:
                return self.employee_dao.check_employee_login(employee)
        raise LoginFailed("Login was not successful, please try again.")
