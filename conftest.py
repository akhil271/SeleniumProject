# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import requests

# ----------------------------
# WebDriver Fixture
# ----------------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# ----------------------------
# Login Fixture
# ----------------------------
@pytest.fixture
def login(driver):
    """Returns a logged-in driver"""
    driver.get("https://automationexercise.com/login")  # Login page URL
    login_page = LoginPage(driver)
    login_page.login("", "")  # Use your credentials
    yield driver
    # Optional: logout after test

# ----------------------------
# SSL check for tests requiring network
# ----------------------------
def pytest_runtest_setup(item):
    """Skip tests marked with 'requires_ssl' if SSL fails"""
    if "requires_ssl" in item.keywords:
        try:
            requests.get(
                "https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build.json",
                timeout=5
            )
        except requests.exceptions.SSLError:
            pytest.skip("Skipping test: SSL verification failed")
        except requests.exceptions.RequestException:
            pytest.skip("Skipping test: Network unavailable or request failed")
