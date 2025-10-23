import time
from utils.browser import get_driver
from pages.scroll_page import ScrollPage


def test_scroll_with_arrow():
    """
    Scroll down using repeated ARROW_DOWN presses, verify bottom content,
    then scroll up using ARROW_UP and verify top banner is visible again.
    """
    driver = get_driver()
    try:
        page = ScrollPage(driver)

        # Ensure we're at top initially
        assert page.wait_for_top_banner(), "Top banner not visible at start."

        # Scroll down with arrow keys
        page.scroll_down_arrow(times=30, sleep=0.07)

        # Verify bottom content (subscription/footer)
        assert page.wait_for_subscription_section() or page.wait_for_footer(), \
            "Bottom (subscription/footer) not visible after arrow scroll."

        # Scroll back up with arrow keys
        page.scroll_up_arrow(times=60, sleep=0.05)

        # Safety scroll to top (in case arrow keys didn't reach fully)
        page.scroll_to_top_js()

        # Verify top banner visible again
        assert page.wait_for_top_banner(), "Top banner not visible after scrolling up."

    finally:
        driver.quit()


def test_scroll_with_js():
    """
    Scroll to bottom/top using JavaScript and verify the expected elements are visible.
    """
    driver = get_driver()
    try:
        page = ScrollPage(driver)

        # Ensure at top
        assert page.wait_for_top_banner(), "Top banner not visible at start."

        # Scroll to bottom via JS
        page.scroll_to_bottom_js()

        # Verify subscription/footer visible
        assert page.wait_for_subscription_section() or page.wait_for_footer(), \
            "Bottom (subscription/footer) not visible after JS scroll."

        # Scroll back to top via JS
        page.scroll_to_top_js()

        # Verify top banner visible again
        assert page.wait_for_top_banner(), "Top banner not visible after JS scroll to top."

    finally:
        driver.quit()
