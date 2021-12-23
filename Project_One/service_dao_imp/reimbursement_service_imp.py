from Project_One.custom_exceptions.incorrect_login import LoginFailed
from Project_One.custom_exceptions.pass_the_length_character_limit import CharacterLimitHasPassedException
from Project_One.custom_exceptions.manager_id_not_found import ManagerIdNotFoundException
from Project_One.custom_exceptions.reimbursement_duplicate_exception import ReimbursementIdDuplicationException
from Project_One.custom_exceptions.employee_id_does_not_exist import EmployeeIdDoesNotExistException
from Project_One.custom_exceptions.reimbursement_not_found import ReimbursementDoesNotExistException
from Project_One.custom_exceptions.numeric_value import MustBeANumericValue
from Project_One.custom_exceptions.invalid_approval import InvalidApprovalException
from Project_One.custom_exceptions.incorrect_information import IncorrectCredentials
from Project_One.custom_exceptions.negative_numbers import NoNegativeNumbers
from Project_One.service_dao.reimbursement_service import ReimbursementServiceDAO
from Project_One.dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from Project_One.entities.reimbursement import Reimbursement


class ReimbursementServiceImp(ReimbursementServiceDAO):
    def __init__(self, reimbursement_dao: ReimbursementDAOImp):
        self.reimbursement_dao = reimbursement_dao

    def service_create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        if reimbursement.approval == "Pending":
            if type(reimbursement.reimbursement) == int:
                if reimbursement.reimbursement >= 0:
                    return self.reimbursement_dao.create_get_reimbursement(reimbursement)
                raise NoNegativeNumbers("Reimbursement must not contain any negative numbers.")
            raise MustBeANumericValue("Reimbursement must be an integer.")
        raise InvalidApprovalException("Invalid approval.")

    def service_select_get_reimbursement_id(self, reimbursement_id: int) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement_id:
                return self.reimbursement_dao.select_get_reimbursement_id(reimbursement_id)
        raise ReimbursementDoesNotExistException("Reimbursement ID does not exist")

    def service_select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        return self.reimbursement_dao.select_get_all_reimbursement_information()

    def service_select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.employee_id == employee_id:
                return self.reimbursement_dao.select_reimbursement_by_employee_id(employee_id)
        raise EmployeeIdDoesNotExistException("Employee Id does not exist")

    #create booleans for manager id = false, and employee id = false..
    def service_approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement.reimbursement_id:
                if existing_reimbursement.manager_id == reimbursement.manager_id:
                    if existing_reimbursement.employee_id == reimbursement.employee_id:
                        if reimbursement.approval == "Approve":
                            return self.reimbursement_dao.approve_reimbursement(reimbursement)
                        raise InvalidApprovalException("Invalid approval")
                    raise EmployeeIdDoesNotExistException("Employee Id does not exist")
                raise ManagerIdNotFoundException("Manager ID does not exist")

    def service_deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement.reimbursement_id:
                if existing_reimbursement.manager_id == reimbursement.manager_id:
                    if existing_reimbursement.employee_id == reimbursement.employee_id:
                        if reimbursement.approval == "Denied":
                            return self.reimbursement_dao.approve_reimbursement(reimbursement)
                        raise InvalidApprovalException("Invalid approval")
                    raise EmployeeIdDoesNotExistException("Employee ID was not found")
                raise ManagerIdNotFoundException("Manager ID does not exist")

    # def service_update_comment_reimbursement_manager_comment(self, reimbursement: Reimbursement) -> Reimbursement:
    #     reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
    #     for existing_reimbursement in reimbursement_list:
    #         if existing_reimbursement.reimbursement_id == reimbursement.reimbursement_id:
    #             if existing_reimbursement.manager_id == reimbursement.manager_id:
    #                 if existing_reimbursement.employee_id == reimbursement.employee_id:
    #                     if len(reimbursement.manager_comment) <= 200:
    #                         return self.reimbursement_dao.update_comment_reimbursement_manager_comment(reimbursement)
    #                     raise CharacterLimitHasPassedException("Character limited was passed.")
    #                 raise EmployeeIdDoesNotExistException("Employee ID was not found")
    #             raise ManagerIdNotFoundException("Manager ID does not exist")

    def service_get_all_pending_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.manager_id == manager_id:
                if existing_reimbursement.approval == "Pending":
                    return self.reimbursement_dao.get_all_pending_reimbursements_by_manager_id(manager_id)
        raise ManagerIdNotFoundException("Manager ID does not exist")

    def service_get_past_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.select_get_all_reimbursement_information()
        for existing_reimbursements in reimbursement_list:
            if existing_reimbursements.manager_id == manager_id:
                if existing_reimbursements.approval != "Pending":
                    return self.reimbursement_dao.get_past_reimbursements_by_manager_id(manager_id)
        raise ManagerIdNotFoundException("Manager ID does not exist")

    def service_view_reimbursements_statistics(self, reimbursement: Reimbursement):
        pass

    def service_update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        result = self.reimbursement_dao.update_reimbursement(reimbursement)
        return result

    # def get_average_reimbursement_lay(self):
    #     requests = self.reimbursement_dao.select_get_all_reimbursement_information()
    #     payouts = []
    #     for results in requests:
    #         if results.approval == 1:
    #             payouts.append(results.reimbursement)
    #     return max(payouts)

    def get_number_of_reimbursement_requests_total(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        return len(requests)

    def get_number_of_reimbursement_requests_pending(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        pending = []
        for p in requests:
            if p.approval == "Pending":
                pending.append(p)
        return len(pending)

    def get_number_of_reimbursement_requests_approved(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        approved = []
        for a in requests:
            if a.approval == "Approve":
                approved.append(a)
        return len(approved)

    def get_number_of_reimbursement_requests_denied(self):
        requests = self.reimbursement_dao.select_get_all_reimbursement_information()
        denied = []
        for d in requests:
            if d.approval == "Denied":
                denied.append(d)
        return len(denied)
