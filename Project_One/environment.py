from behave.runner import Context
from selenium import webdriver
from page_object_models.login_page import LoginPage
from page_object_models.employee_page import Employeepage
from page_object_models.manager_page import Managerpage


def before_all(context: Context):
    context.driver = webdriver.Chrome("Project_One/chromedriver.exe")
    context.login_page = LoginPage(context.driver)
    context.employee_page = Employeepage(context.driver)
    context.manager_page = Managerpage(context.driver)


def after_all(context):
    context.driver.quit()
