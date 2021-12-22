from abc import ABC, abstractmethod
from Project_One.entities.employees import Employee


class EmployeeServiceDAO(ABC):

    # @abstractmethod
    # def service_get_employee_information(self, employee_id: int) -> Employee:
    #     pass

    @abstractmethod
    def service_get_employee_by_username(self, username: str) -> Employee:
        pass

    @abstractmethod
    def service_get_all_employee_information(self) -> list[Employee]:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def service_check_employee_login(self, employee: Employee) -> Employee:
        pass
