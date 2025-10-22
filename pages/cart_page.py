from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from pages.base_page import BasePage

class CartPage(BasePage):
    VIEW_CART_BTN = (By.XPATH, "//u[contains(text(),'View Cart')]")
    PRODUCT_NAME_IN_CART = (By.XPATH, "//td[@class='cart_description']//a")
    CART_QUANTITY_ELEMENT = (By.XPATH, "//td[@class='cart_quantity']/button")
    REMOVE_BTN = (By.XPATH, "//a[@class='cart_quantity_delete']")

    # -----------------------
    # Hide ads
    # -----------------------
    def hide_ads(self):
        try:
            self.driver.execute_script("""
                const ads = document.querySelectorAll('iframe, .adsbygoogle, #aswift_0, #google_ads_iframe');
                ads.forEach(a => a.style.display = 'none');
            """)
            print("✅ Ads hidden successfully.")
        except Exception as e:
            print(f"⚠️ Could not hide ads: {e}")

    # -----------------------
    # Scroll to element
    # -----------------------
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        return element

    # -----------------------
    # View cart
    # -----------------------
    def view_cart(self):
        try:
            self.hide_ads()
            element = self.scroll_to_element(self.VIEW_CART_BTN)
            if hasattr(self, 'js_click'):
                self.js_click(self.VIEW_CART_BTN)
            else:
                element.click()
            # Wait for cart quantity or product to appear
            self.wait.until(EC.presence_of_element_located(self.CART_QUANTITY_ELEMENT))
            print("✅ Clicked 'View Cart' button successfully.")
        except TimeoutException:
            print("❌ Could not click 'View Cart' or cart did not load")
        except Exception as e:
            print(f"❌ Failed to click 'View Cart' button: {e}")
        time.sleep(1)

    # -----------------------
    # Get product quantity
    # -----------------------
    def get_product_quantity_in_cart(self):
        self.view_cart()
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.CART_QUANTITY_ELEMENT))
            qty_text = element.get_attribute("value").strip() if element.tag_name.lower() == "input" else element.text.strip()
            quantity = int(qty_text)
            print(f"🛒 Quantity in cart: {quantity}")
            return quantity
        except Exception as e:
            print(f"❌ Could not get cart quantity: {e}")
            return 0

    # -----------------------
    # Get product names
    # -----------------------
    def get_product_names_in_cart(self):
        self.view_cart()
        try:
            products = self.driver.find_elements(*self.PRODUCT_NAME_IN_CART)
            names = [p.text.strip() for p in products]
            print(f"🛒 Products in cart: {names}")
            return names
        except Exception as e:
            print(f"❌ Could not get product names: {e}")
            return []

    # -----------------------
    # Remove product
    # -----------------------
    def remove_product(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.REMOVE_BTN))
            element.click()
            time.sleep(1)
            print("🗑️ Product removed from cart")
        except Exception as e:
            print(f"❌ Could not remove product: {e}")

    # -----------------------
    # Clear cart
    # -----------------------
    def clear_cart(self):
        self.view_cart()
        retry = 0
        while not self.is_cart_empty() and retry < 10:
            try:
                remove_buttons = self.driver.find_elements(*self.REMOVE_BTN)
                if not remove_buttons:
                    break
                for btn in remove_buttons:
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, btn.get_attribute("xpath") or "//a[@class='cart_quantity_delete']")))
                    btn.click()
                    time.sleep(1)
                self.view_cart()  # refresh cart
            except Exception as e:
                print(f"⚠️ Retry removing product failed: {e}")
            retry += 1
        print("✅ Cart cleared before test")

    # -----------------------
    # Check if cart is empty
    # -----------------------
    def is_cart_empty(self):
        try:
            products = self.driver.find_elements(*self.PRODUCT_NAME_IN_CART)
            empty = len(products) == 0
            print(f"🛒 Cart empty: {empty}")
            return empty
        except Exception as e:
            print(f"❌ Could not check if cart is empty: {e}")
            return False
