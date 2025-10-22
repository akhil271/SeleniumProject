from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_products_page(self):
        """Click the 'Products' link to open the products listing page."""
        self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_LINK)).click()
        print("✅ Clicked on Products link")

    def search_product(self, product_name):
        """Search for a product on the products page."""
        self.open_products_page()

        # Wait for search box to appear
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys(product_name)
        print(f"🔍 Searching for: {product_name}")

        # Click search
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        print("✅ Search button clicked")
