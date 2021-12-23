import time
from behave import Given, When, Then


@Given(u'the manager is on the manager page')
def manager_log_in(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")
    context.login_page.select_enter_username().send_keys("ericsuu")
    context.login_page.select_enter_password().send_keys("ericrules")
    context.login_page.select_click_login().click()


@When(u'the manager enters approve onto approval input box on one reimbursement')
def manager_enters_approve(context):
    time.sleep(1)
    context.manager_page.select_approval("Approve")


@When(u'the manager inputs a managerComment onto managerComment input box in the one reimbursement')
def manager_enters_comment(context):
    time.sleep(1)
    context.manager_page.select_manager_comment("Valid reason")


@When(u'the manager clicks the approve button on one reimbursement')
def manager_click_approve(context):
    time.sleep(1)
    context.manager_page.select_approve_button("Approve").click()


@Then(u'one reimbursement is approved and sent to the previous reimbursements')
def manager_refreshes_page(context):
    time.sleep(1)
    assert context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")


# for the disapproval
@When(u'the manager enters denied onto approval input box on one reimbursement')
def manager_enters_denied(context):
    time.sleep(1)
    context.manager_page.select_approval("Denied")


@When(u'When the manager inputs a managerComment onto managerComment input box in the one reimbursement')
def manager_enters_comment(context):
    time.sleep(1)
    context.manager_page.select_manager_comment("Invalid reason")


@When(u'the manager clicks the deny button')
def manager_click_disapprove(context):
    time.sleep(1)
    context.manager_page.select_denied_button("Deny").click()


@Then(u'one reimbursement is disapproved and sent to the previous reimbursements')
def manager_refreshes_page(context):
    time.sleep(1)
    assert context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/login.html")
