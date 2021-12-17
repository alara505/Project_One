from Project_One.entities.reimbursement import Reimbursement
from Project_One.dao.reimbursement_dao import ReimbursementDAO
from Project_One.util.database_connection import connection
from Project_One.custom_exceptions.incorrect_login import LoginFailed


# To make it more robust add update to have employee change their reimbursement after submitting.

class ReimbursementDAOImp(ReimbursementDAO):

    # This is for the employee to create their reimbursement.
    def create_get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'insert into "Project_one".reimbursement values(default, %s, %s, %s, %s, %s, %s) returning reimbursement_id'
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.employee_id, reimbursement.manager_id, reimbursement.reimbursement, reimbursement.reason,
            reimbursement.approval, reimbursement.manager_comment))
        connection.commit()
        reimbursement_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = reimbursement_id
        return reimbursement

    # This is to grab the specific reimbursement row from their reimbursement id
    def select_get_reimbursement_id(self, reimbursement_id) -> Reimbursement:
        sql = 'select * from "Project_one".reimbursement where reimbursement_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        reimbursement_record = cursor.fetchone()
        reimbursement = Reimbursement(*reimbursement_record)
        return reimbursement

    # This is to grab all the reimbursements from the database
    def select_get_all_reimbursement_information(self) -> list[Reimbursement]:
        sql = 'select * from "Project_one".reimbursement'
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    # This method is to check the employee id who created an reimbursement
    def select_reimbursement_by_employee_id(self, employee_id) -> list[Reimbursement]:
        sql = 'select * from "Project_one".reimbursement where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimbursement_record = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_record:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    # This method for more robust, but it's to grab all the approval requests from the managers
    def get_all_reimbursements_by_approval(self, approval: str) -> list[Reimbursement]:
        pass

    # this method is for the manager to approve their request.
    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'update "Project_one".reimbursement set approval = %s where reimbursement_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.approval, reimbursement.reimbursement_id])
        connection.commit()
        return reimbursement

    # This method is for the manager to deny their request.
    def deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'update "Project_one".reimbursement set approval = %s where reimbursement_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.approval, reimbursement.reimbursement_id])
        connection.commit()
        return reimbursement

    # This method is for the employee to adjust their reimbursement, and reason.
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'update "Project_one".reimbursement set employee_id = %s, manager_id = %s, reimbursement = %s, reason = %s, approval = %s, manager_comment = %s where reimbursement_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.employee_id, reimbursement.manager_id, reimbursement.reimbursement,
            reimbursement.reason, reimbursement.approval, reimbursement.manager_comment, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    # # This is just random method, but it's to select the manager comment, so the employee can check which manager gave that reason. This is for more robust method...
    # def select_comment_reimbursement_manager_comment(self, reimbursement: Reimbursement) -> Reimbursement:
    #     sql = 'select manager_comment = %s from "Project_one".reimbursement where manager_id = %s'
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [reimbursement.manager_comment, reimbursement.manager_id])
    #     reimbursement_record = cursor.fetchone()[0]
    #     reimbursement = Reimbursement(*reimbursement_record)
    #     return reimbursement

    # This method is to have the manager update the table to change/revoke their comment/reason
    def update_comment_reimbursement_manager_comment(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'update "Project_one".reimbursement set manager_comment = %s where manager_id = %s and reimbursement_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.manager_comment, reimbursement.manager_id, reimbursement.reimbursement_id])
        connection.commit()
        return reimbursement
