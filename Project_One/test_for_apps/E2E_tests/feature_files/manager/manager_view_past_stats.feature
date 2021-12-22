Feature: Manager should be able to view the past reimbursements and statistics
  Scenario: As a manager I want to view past reimbursement requests so I can check previous choices
    Given The manager is on manager homepage or pending page
    When The manager clicks past page
    Then The manager should be redirected to the past page with title Manager Past Page


  Scenario: As a manager I want to view statistics so I can reference various Data
    Given The manager is on manager past page
    When The manager clicks home
    Then The manager should be redirected to the homepage with the title Manager Homepage