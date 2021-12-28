from behave import Given, When, Then
import time


# Project_One/feature_files/manager_login.feature
@Given(u'the manager is on the login page')
def manager_get_login_page(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")


@When(u'the manager enters their username in the username input box')
def manager_enter_username(context):
    context.login_page.select_enter_username().send_keys("ericsuu")


@When(u'the manager enters their password in the password input box')
def manager_enter_password(context):
    context.login_page.select_enter_password().send_keys("ericrules")


@When(u'the manager clicks on the Login button')
def manager_click_login(context):
    context.login_page.select_click_login().click()


@Then(u'the manager should be logged in and redirected to the manager home page')
def manager_check_page_url(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Manager Page"
