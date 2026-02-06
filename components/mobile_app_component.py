import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

class MobileAppComponent:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.root = self.page.locator("div.mobile_apps")
                
        self.promotion_title = self.root.get_by_text("Get The App!")
        self.promotion_desc = self.root.get_by_text("Our app has all your travel needs covered")
        
        self.playstore_button = self.root.get_by_role("link", name="PLAYSTORE")
        self.appstore_button = self.root.get_by_role("link", name="APP STORE")
        
        self.mobile_mockup_img = self.root.get_by_role("img", name="app")

    def click_playstore_button(self) -> None:
        logger.info("[ACTION] Clicking on 'Google Play Store' button...")
        self.playstore_button.click()
        logger.info("[SUCCESS] 'Google Play Store' button clicked.")

    def click_appstore_button(self) -> None:
        logger.info("[ACTION] Clicking on 'Apple App Store' button...")
        self.appstore_button.click()
        logger.info("[SUCCESS] 'Apple App Store' button clicked.")