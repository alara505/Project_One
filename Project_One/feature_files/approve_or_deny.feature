Feature: Manager approve or deny a reimbursement.
  Scenario: as a manager, I should be to approve reimbursement requests and leave comment because they are legitimate
    Given the manager is on the manager page
    When the manager enters approve onto approval input box on one reimbursement
    When the manager inputs a managerComment onto managerComment input box in the one reimbursement
    When the manager clicks the approve button
    Then one reimbursement is approved and sent to the previous reimbursements


  Scenario: as a manager, I should be able to deny reimbursement requests and leave comment because they are illegitimate
    Given the manager is on the manager page
    When the manager enters denied onto approval input box on one reimbursement
    When the manager inputs a managerComment onto managerComment input box in the one reimbursement
    When the manager clicks the deny button
    Then one reimbursement is disapproved and sent to the previous reimbursements