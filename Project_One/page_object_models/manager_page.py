from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Managerpage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_reimbursement_id(self):
        element: WebElement = self.driver.find_element(By.ID, "ReimbursementIdInput")
        return element

    def select_employee_id(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeIdInput")
        return element

    def select_manager_id(self):
        element: WebElement = self.driver.find_element(By.ID, "managerIdInput")
        return element

    def select_reimbursement(self):
        element: WebElement = self.driver.find_element(By.ID, "requestReimbursementInput")
        return element

    def select_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reason")
        return element

    def select_approval(self):
        element: WebElement = self.driver.find_element(By.ID, "approval")
        return element

    def select_manager_comment(self):
        element: WebElement = self.driver.find_element(By.ID, "managerComment")
        return element

    def select_approve_button(self):
        element: WebElement = self.driver.find_element(By.ID, "Approvebutton")
        return element

    def select_denied_button(self):
        element: WebElement = self.driver.find_element(By.ID, "Denybutton")
        return element

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutbutton")
        return element
