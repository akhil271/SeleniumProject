# tests/test_add_to_cart.py
import time
import pytest
from utils.browser import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.csv_reader import read_csv  # Make sure your CSV reader is here

@pytest.mark.sanity
def test_add_to_cart():
    driver = get_driver()
    driver.get("https://automationexercise.com/")
    time.sleep(2)

    # --- READ USERS FROM CSV ---
    test_data = read_csv("test_data/users.csv")  # CSV should have columns: email,password
    email = test_data[0]["email"]
    password = test_data[0]["password"]

    # --- LOGIN ---
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login(email, password)
    print(" Login successful")
    time.sleep(2)

    # --- INITIALIZE PAGES ---
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    # --- CLEAR CART BEFORE STARTING ---
    cart_page.view_cart()
    retry = 0
    while not cart_page.is_cart_empty() and retry < 5:
        cart_page.remove_product()
        time.sleep(1)
        retry += 1
    print(" Cart cleared before test")

    # --- NAVIGATE BACK TO PRODUCTS PAGE ---
    driver.get("https://automationexercise.com/products")
    time.sleep(2)

    # --- OPEN FIRST PRODUCT ---
    product_page.open_first_product()
    time.sleep(1)

    # --- SET QUANTITY ---
    product_page.set_quantity(2)
    time.sleep(1)

    # --- ADD TO CART ---
    product_page.add_product_to_cart()
    print(" Product added to cart")
    time.sleep(2)

    # --- VIEW CART AND VERIFY ---
    cart_page.view_cart()
    time.sleep(2)

    # Verify product name
    products_in_cart = cart_page.get_product_names_in_cart()
    assert "Blue Top" in products_in_cart, f" Product not found in cart: {products_in_cart}"
    print(" Product verified in cart")

    # Verify quantity
    qty_in_cart = cart_page.get_product_quantity_in_cart()
    assert qty_in_cart == 2, f" Expected quantity 2 but got {qty_in_cart}"
    print(" Product quantity verified in cart")

    driver.quit()
    print(" Browser closed")
