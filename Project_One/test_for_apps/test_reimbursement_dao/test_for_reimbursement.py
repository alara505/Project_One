from Project_One.dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from Project_One.entities.reimbursement import Reimbursement

new_reimbursement = Reimbursement(4, 1, 1, 1000.00, "Games", "Pending", "")
reimbursement_dao = ReimbursementDAOImp()

employee_reimbursement = Reimbursement(0, 1, 2, 50, "Testing", "Pending", "This is a plain test")
approve_reimbursement = Reimbursement(1, 2, 2, 590.09, "Repaired the company vehicle", "Approved", "")
deny_reimbursement = Reimbursement(2, 1, 1, 200, "Snacks", "Denied", "")
comment_reimbursement = Reimbursement(2, 2, 1, 5, "Snacks", "Approve", "Not valid reason")
update_reimbursement = Reimbursement(3, 3, 3, 500, "Shoes", "Pending", "Manager comment")


def test_create_reimbursement_success():
    result = reimbursement_dao.create_get_reimbursement(new_reimbursement)
    assert result


def test_get_reimbursement_by_id_success():
    show = reimbursement_dao.select_get_reimbursement_id(1)
    assert show.reimbursement_id == 1


def test_get_all_reimbursement_success():
    elist = reimbursement_dao.select_get_all_reimbursement_information()
    return len(elist) >= 2


def test_get_all_reimbursement_by_employee_id_success():
    employee_reimbursement_list = reimbursement_dao.select_reimbursement_by_employee_id(3)
    assert len(employee_reimbursement_list) >= 1


def test_approve_reimbursement_by_id_success():
    approved_reimbursement = reimbursement_dao.approve_reimbursement(approve_reimbursement)
    assert approved_reimbursement


def test_deny_reimbursements_by_id_success():
    denied_reimbursement = reimbursement_dao.deny_reimbursement(deny_reimbursement)
    assert denied_reimbursement


def test_update_reimbursement_success():
    updated_reimbursement = reimbursement_dao.update_reimbursement(update_reimbursement)
    assert updated_reimbursement

#
# def test_comment_reimbursement_manager_comment():
#     manager_comment = reimbursement_dao.select_comment_reimbursement_manager_comment(comment_reimbursement)
#     assert manager_comment
