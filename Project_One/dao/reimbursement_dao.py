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

    # @abstractmethod
    # def get_all_reimbursements_by_approval(self, approval: str) -> list[Reimbursement]:
    #     pass

    @abstractmethod
    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # @abstractmethod
    # def update_comment_reimbursement_manager_comment(self, reimbursement: Reimbursement) -> Reimbursement:
    #     pass

    @abstractmethod
    def get_all_pending_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_past_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_reimbursements_statistics(self, reimbursement: Reimbursement):
        pass


