from behave import Given, When, Then
import time


# Project_One/feature_files/system_login.feature
@Given(u'the system is on the login page')
def get_login_page(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")


@When(u'the system enters their username in the username input box')
def system_enters_username(context):
    context.login_page.select_enter_username().send_keys("alex101")


@When(u'the system enters a faulty password')
def enter_bad_password(context):
    context.login_page.select_enter_password().send_keys("password")


@When(u'the system clicks the login button')
def system_clicks_submit(context):
    context.login_page.select_click_login().click()


@Then(u'a login errors pops')
def error_pop_check(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Invalid username or password"
    context.driver.switch_to.alert.accept()
