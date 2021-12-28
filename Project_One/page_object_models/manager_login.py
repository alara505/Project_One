from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerLogin:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_enter_username(self):
        element: WebElement = self.driver.find_element(By.ID, "username")
        return element

    def select_enter_password(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def select_click_login(self):
        element: WebElement = self.driver.find_element(By.ID, "button")
        return element
