from behave import Given, When, Then
import time


# run this behave Project_One/feature_files/employee_login.feature

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
