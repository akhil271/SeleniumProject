# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    """Returns a logged-in driver"""
    driver.get("https://automationexercise.com/login")  # Login page URL
    login_page = LoginPage(driver)
    login_page.login("akhildadhich9@gmail.com", "Akhil123")  # Use your credentials
    yield driver
    # Optional: logout after test
