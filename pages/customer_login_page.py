import logging
from playwright.sync_api import Page

from pages.base_page import BasePage
from components.login_form_component import LoginFormComponent

logger = logging.getLogger(__name__)

class CustomerLoginPage(BasePage):

    URL = "https://www.phptravels.net/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form = LoginFormComponent(self.page)

    def navigate(self) -> None:
        logger.info(f"[ACTION] Navigating to URL: '{self.URL}'...")
        self.page.goto(self.URL)
        logger.info(f"[SUCCESS] Navigation to URL: '{self.URL}' completed.")