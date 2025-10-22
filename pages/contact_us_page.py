from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from pages.base_page import BasePage

class ContactUsPage(BasePage):

    # Locators
    CONTACT_LINK = (By.LINK_TEXT, "Contact us")
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_INPUT = (By.ID, "message")
    UPLOAD_FILE = (By.NAME, "upload_file")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SUCCESS_TEXT = (By.CSS_SELECTOR, ".status.alert.alert-success")

    # Navigate to Contact Us Page
    def go_to_contact_us(self):
        self.wait.until(EC.presence_of_element_located(self.CONTACT_LINK))
        self.click(self.CONTACT_LINK)

    # Fill and Submit Form
    def submit_contact_form(self, name, email, subject, message):
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.SUBJECT_INPUT, subject)
        self.type_text(self.MESSAGE_INPUT, message)
        self.click(self.SUBMIT_BUTTON)

        # Dynamically handle alert if it appears
        try:
            alert = self.wait.until(lambda d: d.switch_to.alert)
            alert_text = alert.text
            alert.accept()
            print(f"✅ Alert handled: {alert_text}")
        except TimeoutException:
            print("⚠️ No alert appeared, continuing...")

        # Wait for success message dynamically
        try:
            success_element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TEXT))
            return success_element.text.strip()
        except TimeoutException:
            print("❌ Success message not found!")
            return ""
