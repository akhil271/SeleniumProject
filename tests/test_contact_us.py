import time
from utils.browser import get_driver
from pages.contact_us_page import ContactUsPage


def test_contact_us():
    driver = get_driver()
    driver.get("https://automationexercise.com")
    time.sleep(3)  # wait for homepage load

    contact_page = ContactUsPage(driver)
    contact_page.go_to_contact_us()

    success_msg = contact_page.submit_contact_form(
        name="Akhil Dadhich",
        email="akhildadhich9@gmail.com",
        subject="Test Subject",
        message="Hi, this is a test message."
    )

    print("✅ Message shown after form submit:", success_msg)
    assert "Success" in success_msg or "successfully" in success_msg

    driver.quit()
