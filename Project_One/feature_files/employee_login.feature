Feature: Employee Login


  Scenario: As an employee I want to login so I can manage my reimbursements
    Given The employee is on login page
    When The employee enters their username in the username input box
    When The employee enters their password in the password input box
    When The employee clicks on the Login button
    Then The employee should be logged in and redirected to the employee home page

  Scenario: As a manager I want to login so that I can manage my reimbursements
    Given the manager is on the login page
    When the manager enters their username in the username input box
    When the manager enters their password in the password input box
    When the manager clicks on the Login button
    Then the manager should be logged in and redirected to the manager home page


  Scenario: as the system, I should reject failed login attempts
    Given the employee is on the login page
    When the employee enters their username in the username input box
    When the employee enters a faulty password
    When the employee clicks the login button
    Then a login errors pops