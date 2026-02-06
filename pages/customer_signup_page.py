import logging
from playwright.sync_api import Page

from pages.base_page import BasePage
from helpers.common_helper import mask_text
from models.data_models import CustomerSignupData

logger = logging.getLogger(__name__)

class CustomerSignupPage(BasePage):

    URL = "https://www.phptravels.net/signup"

    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = self.page.get_by_role("textbox", name="First Name")
        self.last_name_input = self.page.get_by_role("textbox", name="Last Name")
        self.country_dropdown = self.page.locator("button[data-bs-toggle='dropdown']")
        self.country_search_input = self.page.get_by_role("combobox", name="Search")
        self.phone_input = self.page.get_by_role("spinbutton", name="Phone")
        self.email_input = self.page.get_by_role("textbox", name="Email Address")
        self.password_input = self.page.get_by_role("textbox", name="Password")
        
        self.captcha_frame = self.page.locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]")
        self.captcha_frame_selector = "iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]"
        self.captcha_checkbox = self.captcha_frame.content_frame.locator("#checkbox")
        
        self.signup_button = self.page.get_by_role("button", name="Signup", exact=True)
        self.loading_spinner = self.page.get_by_role("button", name="Creating account...")

    def navigate(self) -> None:
        logger.info(f"[ACTION] Navigating to URL: '{self.URL}'...")
        self.page.goto(self.URL)
        logger.info(f"[SUCCESS] Navigation to URL: '{self.URL}' completed.")

    def enter_first_name(self, first_name: str) -> None:
        logger.info(f"[INPUT] Entering first name: '{first_name}'...")
        self.first_name_input.fill(first_name)
        logger.info("[SUCCESS] First name entered.")

    def enter_last_name(self, last_name: str) -> None:
        logger.info(f"[INPUT] Entering last name: '{last_name}'...")
        self.last_name_input.fill(last_name)
        logger.info("[SUCCESS] Last name entered.")

    def select_country(self, country_name: str) -> None:
        logger.info(f"[INPUT] Selecting country: '{country_name}'...")
        self.country_dropdown.click()
        self.country_search_input.fill(country_name)
        self.page.get_by_role("option", name=country_name).first.click()
        logger.info(f"[SUCCESS] Country '{country_name}' selected.")

    def enter_phone(self, phone: str) -> None:
        logger.info(f"[INPUT] Entering phone number: '{phone}'...")
        self.phone_input.fill(phone)
        logger.info("[SUCCESS] Phone number entered.")

    def enter_email(self, email: str) -> None:
        logger.info(f"[INPUT] Entering email address: '{email}'...")
        self.email_input.fill(email)
        logger.info("[SUCCESS] Email address entered.")

    def enter_password(self, password: str) -> None:
        logger.info(f"[INPUT] Entering password: '{mask_text(password)}'...")
        logger.debug(f"[DEBUG-DATA] Entering password: {password}...")
        self.password_input.fill(password)
        logger.info("[SUCCESS] Password entered.")

    def click_signup_button(self) -> None:
        logger.info("[ACTION] Clicking 'Signup' button...")
        self.signup_button.click()
        logger.info("[SUCCESS] 'Signup' button clicked.")

    def click_captcha_checkbox(self) -> None:
        logger.info("[ACTION] Clicking captcha checkbox...")
        self.captcha_checkbox.click()
        logger.info("[SUCCESS] Captcha checkbox clicked.")

    def wait_for_solve_captcha(self, timeout: int = 30000) -> None:
        logger.info("[EVENT] Waiting for captcha to be solved...")
        self.captcha_frame.content_frame.locator("#checkbox[aria-checked='true']").wait_for(
            state="attached", 
            timeout=timeout
        )
        logger.info("[SUCCESS] Captcha solved.")

    def register_account(self, user_data: CustomerSignupData) -> None:
        logger.info(f"[ACTION] Registering account for email: '{user_data.email}'...")

        self.enter_first_name(user_data.first_name)
        self.enter_last_name(user_data.last_name)
        self.select_country(user_data.country)
        self.enter_phone(user_data.phone)
        self.enter_email(user_data.email)
        self.enter_password(user_data.password)

        self.click_captcha_checkbox()
        self.wait_for_solve_captcha()

        self.click_signup_button()

        logger.info("[SUCCESS] Registration sequence completed.")