import time

from behave import Given, When, Then


@Given(u'the Employee is already logged in')
def step_imp1(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/employee_page.html")


@When(u'the employee clicks on the logout button')
def step_imp1(context):
    time.sleep(1)
    context.employee_logout.select_employee_logout_button("logoutbutton").click()


@Then(u'the employee will return to the login page and have to log back in to view his reimbursements')
def step_imp1(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login Page"
