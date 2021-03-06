Feature: Employee should be able to view past reimbursements and submit new reimbursements
  Scenario: As an employee I want to submit new reimbursement request so I can get money back from the company
    Given The employee is on employee homepage
    When The employee clicks submit page
    When The employee enters information
    When The employee clicks submit reimbursement button
    Then The employee should get a message with success went through


  Scenario: As an employee I want to check reimbursement status so I know if they were approved or denied
    Given The employee is on employee homepage
    When The employee clicks past homepage
    Then The employee should be redirect to the employee page with Employee Past page