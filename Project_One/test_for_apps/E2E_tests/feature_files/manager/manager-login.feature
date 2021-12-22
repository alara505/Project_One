Feature: Manager should be able to login and logout
  Scenario: As a manager I want to log in and so I can approve or deny reimbursements
    Given The manager is on login page
    When The manager enters their credentials
    When The manager clicks submit to login
    Then The manager should be redirect to the manager homepage with the title Manager Homepage

  Scenario: As a manager I want to logout so my information does not remain on the computer screen
    Given The manager is on manager homepage after logging in
    When The manager clicks logout
    Then The manager should be redirected to the login page with the title log in
