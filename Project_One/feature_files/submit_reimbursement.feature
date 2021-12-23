Feature: Submit a reimbursement
  Scenario: As an employee I want to submit a reimbursement to get money back.
    Given the employee is on the employee page
    When the employee enters the employee id
    When the employee enters the manager id
    When the employee enters the reimbursement amount
    When the employee enters the reason
    When the employee clicks the submit button
    Then a new reimbursement is added to the pending reimbursements table


  Scenario: as the system, I should reject negative values for reimbursement requests
    Given the employee is on the employee page
    When the employee enters the employee id
    When the employee enters the manager id
    When the employee enters a negative amount
    When the employee enters the reason
    When the employee clicks the submit button
    Then an reimbursement error pops

  Scenario: as the system, I should reject non-numeric values for the reimbursement requests
    Given the employee is on the employee page
    When the employee enters the employee id
    When the employee enters the manager id
    When the employee enters a non_numeric amount
    When the employee enters a reason
    When the employee clicks the submit button
    Then an amount error pops