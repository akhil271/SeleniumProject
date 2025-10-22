# tests/test_zoom_page.py
import pytest
import time
from pages.zoom_page import ZoomPage

@pytest.mark.sanity
def test_zoom_in_out(driver):
    driver.get("https://automationexercise.com/")
    zoom_page = ZoomPage(driver)

    # --- Zoom in ---
    zoom_page.zoom_in(120)
    time.sleep(2)

    # --- Zoom out ---
    zoom_page.zoom_out(80)
    time.sleep(2)

    # --- Reset ---
    zoom_page.reset_zoom()
    time.sleep(1)

    print("✅ Zoom in/out test completed successfully")
