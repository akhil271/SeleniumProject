# tests/test_place_order.py
import time
import pytest
from selenium.webdriver.common.by import By
from utils.browser import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.sanity
def test_place_order():
    driver = get_driver()

    try:
        # -----------------------
        # LOGIN
        # -----------------------
        login_page = LoginPage(driver)
        login_page.go_to_login()
        login_page.login("akhildadhich9@gmail.com", "Akhil123")
        print("✅ Login successful")
        time.sleep(2)

        # -----------------------
        # INITIALIZE PAGES
        # -----------------------
        product_page = ProductsPage(driver)
        cart_page = CartPage(driver)

        # -----------------------
        # CLEAR CART BEFORE STARTING
        # -----------------------
        cart_page.view_cart()
        retry = 0
        while not cart_page.is_cart_empty() and retry < 5:
            cart_page.remove_product()
            time.sleep(1)
            retry += 1
        print("✅ Cart cleared before test")

        # --- NAVIGATE BACK TO PRODUCTS PAGE ---
        driver.get("https://automationexercise.com/products")
        time.sleep(2)

        # -----------------------
        # OPEN FIRST PRODUCT
        # -----------------------
        product_page.open_first_product()
        time.sleep(1)

        # -----------------------
        # SET QUANTITY AND ADD TO CART
        # -----------------------
        product_page.set_quantity(2)
        product_page.add_product_to_cart()
        print("✅ Product added to cart")
        time.sleep(2)

        # -----------------------
        # VIEW CART AND VERIFY QUANTITY
        # -----------------------
        cart_page.view_cart()
        qty_in_cart = cart_page.get_product_quantity_in_cart()
        assert qty_in_cart == 2, f"❌ Expected quantity 2 but got {qty_in_cart}"
        print("✅ Product quantity verified in cart")

        # -----------------------
        # PROCEED TO CHECKOUT
        # -----------------------
        checkout_btn = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
        cart_page.scroll_to_element(checkout_btn)
        driver.find_element(*checkout_btn).click()
        print("✅ Clicked Proceed To Checkout")
        time.sleep(2)

        # -----------------------
        # PLACE ORDER
        # -----------------------
        try:
            comment_box = driver.find_element(By.NAME, "message")
            comment_box.send_keys("Please deliver between 9 AM - 5 PM")
            print("✅ Added order comment")
        except:
            pass

        place_order_btn = (By.XPATH, "//a[contains(text(),'Place Order')]")
        cart_page.scroll_to_element(place_order_btn)
        driver.find_element(*place_order_btn).click()
        print("✅ Clicked Place Order")
        time.sleep(2)

        # -----------------------
        # PAYMENT INFO
        # -----------------------
        try:
            driver.find_element(By.NAME, "name_on_card").send_keys("Akhil Dadhich")
            driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
            driver.find_element(By.NAME, "cvc").send_keys("123")
            driver.find_element(By.NAME, "expiry_month").send_keys("12")
            driver.find_element(By.NAME, "expiry_year").send_keys("2025")
            driver.find_element(By.ID, "submit").click()
            print("✅ Payment info entered and submitted")
        except Exception as e:
            print(f"⚠️ Payment step skipped: {e}")

        time.sleep(3)
        print("✅ Order placement test completed")

    finally:
        driver.quit()
        print("✅ Browser closed")
