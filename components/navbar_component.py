import re
import logging
from playwright.sync_api import Page, Locator

logger = logging.getLogger(__name__)

class NavbarComponent:

    def __init__(self, page: Page) -> None:

        self.page = page
        self.root = self.page.get_by_role("banner")
        self.currency_pattern = re.compile(r"^(USD|GBP|SAR|EUR|PHP)$")
        
        self.agency_logo = self.root.get_by_role("link", name="logo")

        self.flights_link = self.root.get_by_role("link", name="Flights")
        self.hotels_link = self.root.get_by_role("link", name="Hotels")
        self.tours_link = self.root.get_by_role("link", name="Tours")
        self.cars_link = self.root.get_by_role("link", name="Cars")
        self.visa_link = self.root.get_by_role("link", name="Visa")
        self.blogs_link = self.root.get_by_role("link", name="Blogs")

        self.language_dropdown = self.root.get_by_role("button", name="flag")
        self.currency_dropdown = self.root.get_by_role("button", name=self.currency_pattern)
        self.agents_dropdown = self.root.get_by_role("button", name="Agents")
        self.customer_dropdown = self.root.get_by_role("button", name="Customer")
        
        self.login_link = self.root.locator("ul.dropdown-menu:visible").get_by_role("link", name="Login")
        self.signup_link = self.root.locator("ul.dropdown-menu:visible").get_by_role("link", name="Signup")

    def click_agency_logo(self) -> None:
        logger.info("[ACTION] Clicking 'Agency Logo' in navigation bar...")
        self.agency_logo.click()
        logger.info("[SUCCESS] 'Agency Logo' clicked.")

    def click_navbar_link(self, link_locator: Locator) -> None:
        logger.info(f"[ACTION] Clicking navbar link: {link_locator}...")
        link_locator.click()
        logger.info(f"[SUCCESS] {link_locator} clicked.")

    def select_language(self, language_name: str) -> None:
        logger.info(f"[ACTION] Selecting language: '{language_name}'...")
        self.language_dropdown.click()
        target_lang = self.root.locator("ul.dropdown-menu:visible").get_by_role("link", name=language_name)
        target_lang.click()
        logger.info(f"[SUCCESS] Language '{language_name}' selected.")

    def select_currency(self, currency_code: str) -> None:
        logger.info(f"[ACTION] Selecting currency: '{currency_code}'...")
        self.currency_dropdown.click()
        target_currency = self.root.locator("ul.dropdown-menu:visible").get_by_role("link", name=currency_code)
        target_currency.click()
        logger.info(f"[SUCCESS] Currency '{currency_code}' selected.")

    def go_to_agents_login(self) -> None:
        logger.info("[ACTION] Navigating to 'Agents Login' page...")
        self.agents_dropdown.click()
        self.login_link.click()
        logger.info("[SUCCESS] Navigation to 'Agents Login' page completed.")

    def go_to_agents_signup(self) -> None:
        logger.info("[ACTION] Navigating to 'Agents Signup' page...")
        self.agents_dropdown.click()
        self.signup_link.click()
        logger.info("[SUCCESS] Navigation to 'Agents Signup' page completed.")

    def go_to_customer_login(self) -> None:
        logger.info("[ACTION] Navigating to 'Customer Login' page...")
        self.customer_dropdown.click()
        self.login_link.click()
        logger.info("[SUCCESS] Navigation to 'Customer Login' page completed.")

    def go_to_customer_signup(self) -> None:
        logger.info("[ACTION] Navigating to 'Customer Signup' page...")
        self.customer_dropdown.click()
        self.signup_link.click()
        logger.info("[SUCCESS] Navigation to 'Customer Signup' page completed.")