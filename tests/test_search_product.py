from utils.browser import get_driver
from pages.home_page import HomePage

def test_search_product():
    driver = get_driver()
    home_page = HomePage(driver)
    home_page.search_product("Dress")
    print("✅ Test completed successfully")
    driver.quit()
