from behave import Given, When, Then
import time


# run this behave Project_One/feature_files/employee_login.feature into the terminal for the testing on E2E
@Given(u'The employee is on login page')
def get_login_page(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")


@When(u'The employee enters their username in the username input box')
def employee_enters_username(context):
    context.login_page.select_enter_username().send_keys("alex101")


@When(u'The employee enters their password in the password input box')
def employee_enters_password(context):
    context.login_page.select_enter_password().send_keys("alexrocks")


@When(u'The employee clicks on the Login button')
def employee_clicks_submit(context):
    context.login_page.select_click_login().click()


@Then(u'The employee should be logged in and redirected to the employee home page')
def employee_homepage(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Employee Page"


########################################### For the Manager Login #######################################


@Given(u'the manager is on the login page')
def manager_get_login_page(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")


@When(u'the manager enters their username in the username input box')
def manager_enter_username(context):
    context.login_page.select_enter_username().send_keys("ericsuu")


@When(u'the manager enters their password in the password input box')
def manager_enter_password(context):
    context.login_page.select_enter_password().send_keys("ericrules")


@When(u'the manager clicks the login button')
def manager_click_login(context):
    context.login_page.select_click_login().click()


@Then(u'the manager should be logged in and redirected to the manager home page')
def manager_check_page_url(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Manager Page"


############################################## Sad Test ########################################

@When(u'the employee enters a faulty password')
def enter_bad_password(context):
    context.login_page.select_enter_password().send_keys("password")


@Then(u'a login error pops')
def error_pop_check(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Username or password entered incorrectly."
    context.driver.switch_to.alert.accept()
