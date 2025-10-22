# tests/test_register_existing.py
import pytest
from utils.browser import get_driver
from pages.register_page import RegisterPage

@pytest.mark.sanity
def test_register_existing():
    driver = get_driver()
    driver.get("https://automationexercise.com/")

    register_page = RegisterPage(driver)

    # Try registering an already existing user
    error_msg = register_page.register_existing_user("Akhil", "akhildadhich9@gmail.com")

    # Assert that the proper error message is shown
    assert "Email Address already exist!" in error_msg, f"Expected error message not found: {error_msg}"

    driver.quit()
