from abc import ABC, abstractmethod
from Project_One.entities.reimbursement import Reimbursement
from typing import List


class ReimbursementDAO(ABC):

    @abstractmethod
    def create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        pass

    @abstractmethod
    def select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        pass

    @abstractmethod
    def approve_reimbursement(self, employee_id) -> Reimbursement:
        pass

    @abstractmethod
    def deny_reimbursement(self, employee_id) -> Reimbursement:
        pass

    # @abstractmethod
    # def select_comment_reimbursement_manager_comment(self, manager_id) -> Reimbursement:
    #     pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def update_comment_reimbursement_manager_comment(self, reimbursement: Reimbursement) -> Reimbursement:
        pass


