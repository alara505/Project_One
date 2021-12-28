import time

from behave import Given, When, Then


@Given(u'the manager is on the manager page')
def step_imp1(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/manager_page.html")


@When(u'the manager clicks the logout button')
def step_imp1(context):
    time.sleep(1)
    context.manager_logout.select_manager_logout_button("logoutbutton").click()


@Then(u'the manager is on the login page')
def step_imp1(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login Page"
