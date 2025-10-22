# pages/zoom_page.py
class ZoomPage:
    def __init__(self, driver):
        self.driver = driver

    def zoom_in(self, percentage=150):
        """Zoom in the page"""
        self.driver.execute_script(f"document.body.style.zoom='{percentage}%'")
        print(f"🔍 Zoomed in to {percentage}%")

    def zoom_out(self, percentage=50):
        """Zoom out the page"""
        self.driver.execute_script(f"document.body.style.zoom='{percentage}%'")
        print(f"🔍 Zoomed out to {percentage}%")

    def reset_zoom(self):
        """Reset zoom to normal"""
        self.driver.execute_script("document.body.style.zoom='100%'")
        print("🔄 Reset zoom to 100%")
