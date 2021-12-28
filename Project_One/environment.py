from behave.runner import Context
from selenium import webdriver
from page_object_models.employee_login import EmployeeLogin
from page_object_models.manager_login import ManagerLogin
from page_object_models.submit_reimbursement import SubmitReimbursement
from page_object_models.approve_reimbursement import ApproveReimbursement
from page_object_models.deny_reimbursement import DenyReimbursement
from page_object_models.employee_logout import EmployeeLogout
from page_object_models.manager_logout import ManagerLogout


####### The feature tests ##########
# Project_One/feature_files/employee_login.feature
# Project_One/feature_files/employee_logout.feature
# Project_One/feature_files/manager_login.feature
# Project_One/feature_files/manager_logout.feature
# Project_One/feature_files/submit_reimbursement.feature
# Project_One/feature_files/system_login.feature
# Project_One/feature_files/approve_reimbursement.feature
# Project_One/feature_files/deny_reimbursement.feature


def before_all(context: Context):
    context.driver = webdriver.Chrome("Project_One/chromedriver.exe")
    context.login_page = EmployeeLogin(context.driver)
    context.login_page = ManagerLogin(context.driver)
    context.submit_reimbursement = SubmitReimbursement(context.driver)
    context.approve_reimbursement = ApproveReimbursement(context.driver)
    context.deny_reimbursement = DenyReimbursement(context.driver)
    context.employee_logout = EmployeeLogout(context.driver)
    context.manager_logout = ManagerLogout(context.driver)


def after_all(context):
    context.driver.quit()
