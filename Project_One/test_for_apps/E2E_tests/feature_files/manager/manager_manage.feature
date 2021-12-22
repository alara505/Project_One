Feature Manager should be able to manager reimbursements
  Scenario: As a manager I want to view pending reimbursement request so I can manager them
    Given The manager is on manager home page or past section
    When The manager is directed to pending page
    Then The manager should be redirected to the manager pending page with the title Manager Page


  Scenario: As a manager I want to approve reimbursement requests and leave a comment so I can understand their explanation
    Given The manager is on manager pending page
    When The manager enters comment for approval
    When The manager clicks approve button
    Then The manager will see a message


  Scenario: As a manager I want to reject reimbursement requests and leave a comment so I can let them know why I rejected their reimbursement
    Given The manager is on manager pending page
    When The manager enters comment for rejection
    When The manager clicks denied button
    Then The manager will see a message
