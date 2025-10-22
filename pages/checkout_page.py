# pages/checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.name_input = (By.NAME, "name_on_card")
        self.card_number = (By.NAME, "card_number")
        self.cvc = (By.NAME, "cvc")
        self.exp_month = (By.NAME, "expiry_month")
        self.exp_year = (By.NAME, "expiry_year")
        self.pay_button = (By.ID, "submit")
        self.ORDER_SUCCESS_MSG = (By.XPATH, "//p[contains(text(),'successfully')]")  # adjust text if site changes

    def fill_payment_details(self, name, number, cvc, month, year):
        try:
            self.wait.until(EC.presence_of_element_located(self.name_input)).send_keys(name)
            self.driver.find_element(*self.card_number).send_keys(number)
            self.driver.find_element(*self.cvc).send_keys(cvc)
            self.driver.find_element(*self.exp_month).send_keys(month)
            self.driver.find_element(*self.exp_year).send_keys(year)
            print("✅ Filled payment details")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Could not fill payment details (demo site): {e}")

    def place_order(self):
        try:
            self.driver.find_element(*self.pay_button).click()
            print("✅ Placed the order (demo site, no real success message)")
            time.sleep(2)
        except Exception as e:
            print(f"❌ Could not click Place Order button: {e}")

    def get_order_success_message(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_MSG))
            msg = element.text.strip()
            print(f"✅ Order success message: {msg}")
            return msg
        except Exception as e:
            print(f"⚠️ Could not get order success message (demo site): {e}")
            return ""
