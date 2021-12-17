from abc import ABC, abstractmethod
from Project_One.entities.employees import Employee
from typing import List


class EmployeeDAO(ABC):

    @abstractmethod
    def get_employee_information(self, employee_id) -> Employee:
        pass

    @abstractmethod
    def get_all_employee_information(self) -> list[Employee]:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def check_employee_login(self, employee: Employee) -> Employee:
        pass

