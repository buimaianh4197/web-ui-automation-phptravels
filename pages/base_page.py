import allure
import logging
from playwright.sync_api import Page, Dialog

from components.navbar_component import NavbarComponent
from components.footer_component import FooterComponent
from components.mobile_app_component import MobileAppComponent

logger = logging.getLogger(__name__)

class BasePage:
    
    def __init__(self, page: Page) -> None:
        self.page = page

        self.navbar = NavbarComponent(self.page)
        self.mobile_app = MobileAppComponent(self.page)
        self.footer = FooterComponent(self.page)

    def handle_browser_dialog(self, dialog: Dialog, dialog_result: dict[str, str]) -> None:
        logger.info(f"[EVENT] Browser dialog detected with message: '{dialog.message}'.")
        
        dialog_result["message"] = dialog.message

        allure.attach(
            f"Alert dialog content: {dialog.message}",
            name="Log_Output_DialogContent",
            attachment_type=allure.attachment_type.TEXT
        )

        logger.info(f"[ACTION] Accepting browser dialog: '{dialog.message}'...")
        dialog.accept()
        logger.info("[SUCCESS] Browser dialog accepted.")