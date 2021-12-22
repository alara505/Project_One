Feature: Employee should be able to login and logout
  Scenario: As an employee I want to login so I can check my reimbursements
    Given The employee is on login page
    When The employee enters their credentials
    When The employee clicks the submit login button
    Then The employee is directed to the employee homepage with title Employee Homepage


  Scenario: As an employee I want to logout so my information does not remain on the computer
    Given The employee is on employee homepage after logging in
    When The employee clicks logout
    Then The employe should be redirected to the login page with title Login