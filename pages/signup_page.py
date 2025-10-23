from selenium.webdriver.common.by import By
import time
import random

class SignupPage:
    # Locators
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH, "//button[text()='Signup']")
    ACCOUNT_INFO_TEXT = (By.XPATH, "//*[contains(text(),'Enter Account Information')]")

    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        self.driver.get("https://automationexercise.com/")
        assert "Automation Exercise" in self.driver.title

    def click_signup_login(self):
        self.driver.find_element(*self.SIGNUP_LOGIN_BTN).click()
        time.sleep(2)

    def signup_new_user(self):
        random_email = f"testuser_{random.randint(1000,9999)}@example.com"
        self.driver.find_element(*self.NAME_FIELD).send_keys("Test User")
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(random_email)
        self.driver.find_element(*self.SIGNUP_BTN).click()
        time.sleep(2)
        return random_email

    def verify_signup_page_loaded(self):
        assert "Enter Account Information" in self.driver.page_source
