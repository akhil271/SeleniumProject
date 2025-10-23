from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver(browser_name="chrome"):
    """Factory method to initialize WebDriver for the given browser in headed mode."""
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        options = ChromeOptions()
        # You can still add useful flags if needed:
        # options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Edge(service=EdgeService(), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    return driver
