# pages/register_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RegisterPage(BasePage):
    # Locators
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ERROR_MSG = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")

    # Navigate to Signup/Login page
    def open_signup_page(self):
        self.click(self.LOGIN_LINK)

    # Register an already existing user
    def register_existing_user(self, name, email):
        # Step 1: Click the Signup/Login link
        self.open_signup_page()

        # Step 2: Wait for signup form to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

        # Step 3: Fill form using BasePage.type_text
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.EMAIL_INPUT, email)

        # Step 4: Click signup
        self.click(self.SIGNUP_BUTTON)

        # Step 5: Wait and get error message
        return self.get_text(self.ERROR_MSG)
