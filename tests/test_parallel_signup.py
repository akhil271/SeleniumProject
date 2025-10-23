import pytest
from utils.driver_factory import get_driver
from pages.signup_page import SignupPage


@pytest.fixture(params=["chrome", "edge"])
def driver(request):
    """Launch driver for each browser."""
    driver = get_driver(request.param)
    yield driver
    driver.quit()


def test_signup_in_parallel(driver):
    """Run signup test on all browsers in parallel."""
    signup_page = SignupPage(driver)

    signup_page.open_homepage()
    signup_page.click_signup_login()
    email = signup_page.signup_new_user()
    signup_page.verify_signup_page_loaded()

    print(f"✅ Signup flow passed on {driver.name.capitalize()} with email {email}")
