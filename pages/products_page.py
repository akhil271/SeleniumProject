# pages/products_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from pages.base_page import BasePage

class ProductsPage(BasePage):
    FIRST_PRODUCT = (By.XPATH, "(//a[contains(@href,'product_details')])[1]")
    ADD_TO_CART_BTN = (By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
    QUANTITY_INPUT = (By.NAME, "quantity")
    ADD_CART_CONFIRM_BTN = (By.XPATH, "//button[contains(text(),'Add to Cart')]")

    # -----------------------
    # Open first product
    # -----------------------
    def open_first_product(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
            print("✅ First product opened")
            time.sleep(1)
        except TimeoutException:
            print("❌ Could not open first product: Timeout")
        except Exception as e:
            print(f"❌ Could not open first product: {e}")

    # -----------------------
    # Set quantity
    # -----------------------
    def set_quantity(self, qty=1):
        try:
            input_field = self.wait.until(EC.presence_of_element_located(self.QUANTITY_INPUT))
            input_field.clear()
            input_field.send_keys(str(qty))
            print(f"✅ Quantity set to {qty}")
        except Exception as e:
            print(f"❌ Could not set quantity: {e}")

    # -----------------------
    # Add product to cart
    # -----------------------
    def add_product_to_cart(self):
        try:
            add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN))
            add_btn.click()
            print("✅ Product added to cart")
            time.sleep(1)
        except Exception as e:
            print(f"❌ Could not click 'Add to Cart': {e}")

    # -----------------------
    # Hover and double click (optional)
    # -----------------------
    def hover_and_double_click_add_to_cart(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            element = self.wait.until(EC.presence_of_element_located(self.ADD_TO_CART_BTN))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).double_click(element).perform()
            print("✅ Hovered and double clicked Add to Cart")
        except Exception as e:
            print(f"⚠️ Hover/Double click failed: {e}")
