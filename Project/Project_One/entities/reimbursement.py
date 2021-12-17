class Reimbursement:
    def __init__(self, reimbursement_id: int = 0, employee_id: int = 0, manager_id: int = 0,
                 reimbursement: float = 0.00, reason: str = "", approval: str = 'pending', manager_comment: str = ""):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.reimbursement = reimbursement
        self.reason = reason
        self.approval = approval
        self.manager_comment = manager_comment

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "employeeId": self.employee_id,
            "managerId": self.manager_id,
            "reimbursement": self.reimbursement,
            "reason": self.reason,
            "approval": self.approval,
            "managerComment": self.manager_comment
        }

    def __str__(self):
        return "reimbursement id: {}," \
               " employee id: {}," \
               " manager id: {}," \
               " reimbursement: {}," \
               " reason:{}," \
               " approval: {}," \
               " manager comment: {}".format(self.reimbursement_id, self.employee_id, self.manager_id,
                                             self.reimbursement, self.reason, self.approval, self.manager_comment)
