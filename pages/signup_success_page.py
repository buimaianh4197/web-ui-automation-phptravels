import logging
from playwright.sync_api import Page

from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class SignupSuccessPage(BasePage):

    URL = "https://www.phptravels.net/signup_success"

    def __init__(self, page: Page):
        super().__init__(page)

        self.activate_account_mgs = ["Your account has been created", "Please check your mailbox for activation"]
        self.notification_card = self.page.locator("div").filter(has_text="Your account has been created").nth(2)
