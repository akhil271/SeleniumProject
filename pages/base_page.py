from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # -----------------------
    # Basic actions
    # -----------------------
    def click(self, locator):
        """Normal click after element is clickable"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"✅ Clicked element: {locator}")
        except TimeoutException:
            print(f"❌ Timeout: could not click element {locator}")
        except Exception as e:
            print(f"❌ Error clicking element {locator}: {e}")

    def js_click(self, locator):
        """Click using JavaScript in case normal click fails"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)
            print(f"✅ JS clicked element: {locator}")
        except TimeoutException:
            print(f"❌ Timeout: could not JS click {locator}")
        except Exception as e:
            print(f"❌ JS click error for {locator}: {e}")

    def type_text(self, locator, text):
        """Clear field and type text"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            print(f"✅ Typed text '{text}' into element: {locator}")
        except TimeoutException:
            print(f"❌ Timeout: could not type text into {locator}")
        except Exception as e:
            print(f"❌ Error typing into {locator}: {e}")

    def get_text(self, locator):
        """Get text of an element"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text.strip()
            print(f"📄 Got text '{text}' from {locator}")
            return text
        except TimeoutException:
            print(f"❌ Timeout: could not get text from {locator}")
            return None
        except Exception as e:
            print(f"❌ Error getting text from {locator}: {e}")
            return None

    def is_visible(self, locator):
        """Return True if element visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            print(f"👀 Element visible: {locator}")
            return True
        except TimeoutException:
            print(f"⚠️ Element not visible: {locator}")
            return False

    def scroll_to_element(self, locator):
        """Scroll the page until element is visible"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            print(f"🔽 Scrolled to element: {locator}")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Could not scroll to {locator}: {e}")

    def wait_for_element(self, locator, timeout=10):
        """Wait until element is visible, custom timeout"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            print(f"⏳ Waited and found element: {locator}")
            return element
        except TimeoutException:
            print(f"❌ Timeout waiting for {locator}")
            return None
