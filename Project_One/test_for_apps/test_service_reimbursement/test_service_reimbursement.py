from Project_One.custom_exceptions.employee_id_does_not_exist import EmployeeIdDoesNotExistException
from Project_One.custom_exceptions.invalid_approval import InvalidApprovalException
from Project_One.custom_exceptions.manager_id_not_found import ManagerIdNotFoundException
from Project_One.custom_exceptions.negative_numbers import NoNegativeNumbers
from Project_One.custom_exceptions.numeric_value import MustBeANumericValue
from Project_One.custom_exceptions.reimbursement_not_found import ReimbursementDoesNotExistException
from Project_One.custom_exceptions.pass_the_length_character_limit import CharacterLimitHasPassedException
from Project_One.dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from Project_One.entities.reimbursement import Reimbursement
from Project_One.service_dao_imp.reimbursement_service_imp import ReimbursementServiceImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)

reimbursement_with_bad_approve = Reimbursement(4, 1, 1, 500, "Test Reimbursement", "Test", "")
reimbursement_with_bad_manager_id = Reimbursement(4, 1, 2, 50, "Test Reimbursement", "Approved", "")
reimbursement_with_bad_employee_id = Reimbursement(4, 30, 1, 50, "Food with the bois", "Pending", "")
reimbursement_with_negative_number = Reimbursement(4, 3, 1, -50, "Laptop", "Pending", "")
reimbursement_with_non_numeric = Reimbursement(4, 3, 1, "xyz", "Laptop", "Pending", "")
reimbursement_with_too_many_chars = Reimbursement(4, 2, 1, 500, "Testing", "Approved", "")
reimbursement_with_duplicate_reimbursement_id = Reimbursement(4, 3, 1, 500, "Testing", "Pending", "")


def test_get_reimbursement_by_id_fail():
    try:
        reimbursement_service.service_select_get_reimbursement_id(2000)
        assert False
    except ReimbursementDoesNotExistException as e:
        assert str(e) == "Reimbursement ID does not exist"


def test_get_all_reimbursements_by_employee_id_fail():
    try:
        reimbursement_service.service_select_reimbursement_by_employee_id(3000)
        assert False
    except EmployeeIdDoesNotExistException as e:
        assert str(e) == "Employee Id does not exist"


def test_approve_reimbursement_fail_by_approval():
    try:
        reimbursement_service.service_approve_reimbursement(reimbursement_with_bad_approve)
        assert False
    except InvalidApprovalException as e:
        assert str(e) == "Invalid approval"


def test_approve_reimbursement_fail_by_manager_id():
    try:
        reimbursement_service.service_approve_reimbursement(reimbursement_with_bad_manager_id)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID does not exist"


def test_approve_reimbursement_fail_by_employee_id():
    try:
        reimbursement_service.service_approve_reimbursement(reimbursement_with_bad_employee_id)
        assert False
    except EmployeeIdDoesNotExistException as e:
        assert str(e) == "Employee Id does not exist"


def test_deny_reimbursement_fail_by_approve():
    try:
        reimbursement_service.service_deny_reimbursement(reimbursement_with_bad_approve)
        assert False
    except InvalidApprovalException as e:
        assert str(e) == "Invalid approval"


def test_deny_reimbursement_fail_by_manager_id():
    try:
        reimbursement_service.service_deny_reimbursement(reimbursement_with_bad_manager_id)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID does not exist"


def test_deny_reimbursement_fail_by_employee_id():
    try:
        reimbursement_service.service_deny_reimbursement(reimbursement_with_bad_employee_id)
        assert False
    except EmployeeIdDoesNotExistException as e:
        assert str(e) == "Employee ID was not found"

# Error
# def test_approve_reimbursement_comment_fail_by_too_many_char():
#     try:
#         reimbursement_service.service_update_comment_reimbursement_manager_comment(reimbursement_with_too_many_chars)
#         assert False
#     except CharacterLimitHasPassedException as e:
#         assert str(e) == "Character limited was passed."


# Error( it works but when I start it all together, it fails.
def test_get_all_pending_fail_by_manager_id():
    try:
        reimbursement_service.service_get_all_pending_reimbursements_by_manager_id(50000)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID does not exist"


# Error(It works but when I start it all together, it fails.
def test_get_all_past_fail_by_manager_id():
    try:
        reimbursement_service.service_get_past_reimbursements_by_manager_id(3000)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID does not exist"


# Error(It works but when I start it all together, it fails.
def test_invalid_approve_statement_create_reimbursement_fail():
    try:
        reimbursement_service.service_create_get_reimbursement(reimbursement_with_bad_approve)
        assert False
    except InvalidApprovalException as e:
        assert str(e) == "Invalid approval."


# Error
def test_reimbursement_negative_number_fail():
    try:
        reimbursement_service.service_create_get_reimbursement(reimbursement_with_negative_number)
        assert False
    except NoNegativeNumbers as e:
        assert str(e) == "Reimbursement must not contain any negative numbers."


def test_reimbursement_non_numeric_fail():
    try:
        reimbursement_service.service_create_get_reimbursement(reimbursement_with_non_numeric)
        assert False
    except MustBeANumericValue as e:
        assert str(e) == "Reimbursement must be an integer."
