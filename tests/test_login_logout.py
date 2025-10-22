from utils.browser import get_driver
from pages.login_page import LoginPage
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_excel(file_path):
    """Read the first user from an Excel file and return email and password."""
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    email = sheet["A2"].value  # Assuming first row is headers
    password = sheet["B2"].value
    return email, password

def test_login_logout():
    driver = get_driver()
    driver.get("https://automationexercise.com/")

    # --- READ CREDENTIALS FROM EXCEL ---
    email, password = read_excel("test_data/excel.xlsx")  # path to your Excel file

    login_page = LoginPage(driver)
    login_page.go_to_login()

    # --- WAIT FOR EMAIL FIELD ---
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='login-button']")))

    # --- ENTER CREDENTIALS ---
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_btn.click()

    # --- ASSERT LOGIN SUCCESS ---
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
    assert "Logout" in driver.page_source

    # --- LOGOUT ---
    login_page.logout()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Signup / Login")))
    assert "Signup / Login" in driver.page_source

    driver.quit()
