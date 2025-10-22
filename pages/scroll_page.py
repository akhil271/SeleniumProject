from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ScrollPage:
    """
    Page object that provides scroll helpers and checks for the AutomationExercise page.
    """

    # Locators for checks
    TOP_BANNER = (By.XPATH, "//h2[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'practice website')]")
    SUBSCRIPTION_SECTION = (By.XPATH, "//h2[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'subscription')]")
    FOOTER = (By.TAG_NAME, "footer")

    def __init__(self, driver, wait_seconds: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_seconds)

    # ---------- Arrow-key scrolling ----------
    def scroll_down_arrow(self, times: int = 10, sleep: float = 0.15):
        """
        Press the down arrow key `times` times to scroll down slowly.
        """
        body = self.driver.find_element(By.TAG_NAME, "body")
        for _ in range(times):
            body.send_keys(Keys.ARROW_DOWN)
            time.sleep(sleep)

    def scroll_up_arrow(self, times: int = 10, sleep: float = 0.15):
        """
        Press the up arrow key `times` times to scroll up slowly.
        """
        body = self.driver.find_element(By.TAG_NAME, "body")
        for _ in range(times):
            body.send_keys(Keys.ARROW_UP)
            time.sleep(sleep)

    # ---------- JavaScript scrolling ----------
    def scroll_to_bottom_js(self):
        """Scroll instantly to the bottom of the page using JS."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top_js(self):
        """Scroll instantly to the top of the page using JS."""
        self.driver.execute_script("window.scrollTo(0, 0);")

    # ---------- Visibility checks ----------
    def wait_for_top_banner(self, timeout: int = 10) -> bool:
        """
        Wait for the top banner text to be visible.
        Returns True if found, False on timeout.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self.TOP_BANNER))
            return True
        except Exception:
            return False

    def wait_for_subscription_section(self, timeout: int = 10) -> bool:
        """
        Wait for the subscription section to be visible (bottom area).
        Returns True if found, False on timeout.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_SECTION))
            return True
        except Exception:
            return False

    def wait_for_footer(self, timeout: int = 10) -> bool:
        """Wait for footer presence as an additional bottom-of-page check."""
        try:
            self.wait.until(EC.visibility_of_element_located(self.FOOTER))
            return True
        except Exception:
            return False
