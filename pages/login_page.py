# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Login')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Login')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def is_error_displayed(self):
        """Check if login error message is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return True
        except TimeoutException:
            return False

    def logout(self):
        """Click the Logout link"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
            self.click(self.LOGOUT_LINK)
        except TimeoutException:
            print("⚠️ Logout link not visible!")
