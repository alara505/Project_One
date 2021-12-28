from behave import Given, When, Then
import time


# Project_One/feature_files/system_login.feature
@Given(u'the employee is on the employee page')
def get_login_page(context):
    context.driver.get("file:///C:/Users/Alex/PycharmProjects/Project/Project_One/html_css_js/html/employee_page.html")


@When(u'the employee enters the employee id in the employee id  input box')
def enter_employee_id(context):
    context.submit_reimbursement.select_employee_id().send_keys("1")


@When(u'the employee enters the manager id in the manager id  input box')
def enter_manager_id(context):
    context.submit_reimbursement.select_manager_id().send_keys("1")


@When(u'the employee enters the reimbursement amount in the reimbursement amount  input box')
def enter_reimbursement_amount(context):
    context.submit_reimbursement.select_reimbursement_amount().send_keys("500")


@When(u'the employee enters the reason in the reason  input box')
def enter_reason(context):
    context.submit_reimbursement.select_reason().send_keys("Just cause why not")


@When(u'the employee clicks the submit button')
def click_reimbursement_button(context):
    context.submit_reimbursement.select_submit_button().click()


@Then(u'a new reimbursement is added to the Reimbursement Information')
def submit_reimbursement_button(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Employee Page"
