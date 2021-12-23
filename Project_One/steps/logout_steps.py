import time

from behave import Given, When, Then


@When(u'the employee clicks the logout button')
def step_imp1(context):
    context.employee_page.select_logout_button("logout").click()


@Then(u'the employee is on the login page')
def step_imp1(context):
    time.sleep(1)
    title = context.drive.title
    assert title == "Login Page"


############################################## Manager Logout ##################################

@When(u'the manager clicks the logout button')
def step_imp1(context):
    time.sleep(1)
    context.manager_page.select_logout_button("logout").click()


@Then(u'the manager is on the login page')
def step_imp1(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login Page"
