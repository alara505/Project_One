from abc import ABC, abstractmethod
from Project_One.entities.reimbursement import Reimbursement
from Project_One.dao.reimbursement_dao import ReimbursementDAO
from Project_One.dao_imp.reimbursement_dao_imp import ReimbursementDAOImp

from typing import List


class ReimbursementServiceDAO(ABC):

    @abstractmethod
    def service_create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        pass

    @abstractmethod
    def service_select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_approve_reimbursement(self, employee_id) -> Reimbursement:
        pass

    @abstractmethod
    def service_deny_reimbursement(self, employee_id) -> Reimbursement:
        pass

    # @abstractmethod
    # def select_comment_reimbursement_manager_comment(self, manager_id) -> Reimbursement:
    #     pass

    @abstractmethod
    def service_update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def service_update_comment_reimbursement_manager_comment(self, reimbursement: Reimbursement) -> Reimbursement:
        pass