# tests/test_advanced_actions.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.sanity
def test_advanced_actions():
    # --- Setup driver ---
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://automationexercise.com/products")
        time.sleep(2)

        actions = ActionChains(driver)

        # --- Mouse Hover over first product ---
        first_product = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center'])[1]")
        actions.move_to_element(first_product).perform()
        print("🖱️ Mouse hovered over first product")
        time.sleep(1)

        # --- Double click on first product name ---
        product_name = first_product.find_element(By.TAG_NAME, "p")
        actions.double_click(product_name).perform()
        print("🖱️ Double clicked on product name")
        time.sleep(1)

        # --- Keyboard actions: type in search box, select all, copy, paste ---
        search_box = driver.find_element(By.ID, "search_product")
        search_box.click()
        search_box.send_keys("Dress")
        print("⌨️ Typed 'Dress' in search box")
        time.sleep(1)

        # Select all (Ctrl+A), Copy (Ctrl+C), then clear and Paste (Ctrl+V)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        print("⌨️ Selected all text (Ctrl+A)")
        time.sleep(1)

        actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        print("⌨️ Copied text (Ctrl+C)")
        time.sleep(1)

        search_box.clear()
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        print("⌨️ Pasted text back (Ctrl+V)")
        time.sleep(1)

    finally:
        driver.quit()
        print("✅ Browser closed")

