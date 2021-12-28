Feature: System Login
    Scenario: as the system, I should reject failed login attempts
    Given the system is on the login page
    When the system enters their username in the username input box
    When the system enters a faulty password
    When the system clicks the login button
    Then a login errors pops