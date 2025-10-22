from utils.browser import get_driver
from pages.login_page import LoginPage

def test_login_invalid():
    driver = get_driver()
    driver.get("https://automationexercise.com/")

    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("wrongemail@gmail.com", "wrongpass")

    assert login_page.is_error_displayed() == True

    driver.quit()
