Feature: Manager Login

  Scenario: As a manager I want to login so that I can manage my reimbursements
    Given the manager is on the login page
    When the manager enters their username in the username input box
    When the manager enters their password in the password input box
    When the manager clicks on the Login button
    Then the manager should be logged in and redirected to the manager home page