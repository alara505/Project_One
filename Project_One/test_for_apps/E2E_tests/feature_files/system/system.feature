Feature: System should prevent mal-data and unauthorized activities
  Scenario: As a system I want to reject failed login attempts
    Given The system is on login page
    When The system enters incorrect credentials
    When The system presses enter or clicks submit
    Then The system should see a pop-up window displaying the incorrect credentials


  Scenario: As a system I want to reject negative values for the reimbursement amount so I can pervent mal-data
    Given The system is on submit page
    When The system enters negative number into the amount and other fields
    When The system clicks submit
    Then The system should see a pop-up window displaying negative numbers are not allowed

  Scenario: As a system I want to reject non-numeric values for reimbursement amount so I can pervent mal-data
    Given The system is on submit page
    When The system enters non-numeric values into the amount and other fields
    When The system clicks submit
    Then The system should see a pop-up window displaying non-numeric values are not allowed