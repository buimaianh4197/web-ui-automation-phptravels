import logging
from playwright.sync_api import Page

from helpers.common_helper import mask_text

logger = logging.getLogger(__name__)

class LoginFormComponent:
    
    def __init__(self, page: Page) -> None:
        self.page = page

        self.email_input = self.page.locator("#email")
        self.password_input = self.page.get_by_role("textbox", name="Password")

        self.remember_me_checkbox = self.page.get_by_role("checkbox", name="Remember Me")
        self.remember_me_text = self.page.get_by_text("Remember Me")
        # self.remember_me_checkbox = self.page.locator("span.checkmark")

        self.reset_password_link = self.page.locator("#login").get_by_text("Reset Password")
        self.reset_password_modal = self.page.locator("#forget_pass")
        self.reset_pw_email_input = self.page.get_by_role("dialog", name="Reset Password").get_by_placeholder("name@example.com")
        self.reset_pw_cancel_button = self.page.get_by_role("button", name="Cancel")
        self.reset_pw_reset_button = self.page.get_by_role("button", name="Reset Email")
        self.reset_pw_add_email_alert_msg = "Please add email address to reset password"
        self.reset_pw_invalid_email_alert_msg = "Invalid or no account found with this email"

        self.login_button = self.page.get_by_role("button", name="Login")
        self.signup_button = self.page.get_by_role("link", name="Signup")
        
        self.alert_card = self.page.locator("div.vt-card.error")
        self.not_active_account_alert_msgs = ["Account not active", "Please contact admin to activate your account"]
        self.invalid_login_alert_msgs = ["Invalid Login", "Please check your email and password"]

    def enter_email(self, email: str) -> None:
        logger.info(f"[INPUT] Entering email: '{email}'...")
        self.email_input.fill(email)
        logger.info("[SUCCESS] Email entered.")

    def enter_password(self, password: str) -> None:
        logger.info(f"[INPUT] Entering password: '{mask_text(password)}'...")
        logger.debug(f"[DEBUG-DATA] Entering password: {password}...")
        self.password_input.fill(password)
        logger.info("[SUCCESS] Password entered.")

    def click_login_button(self) -> None:
        logger.info("[ACTION] Clicking 'Login' button...")
        self.login_button.click()
        logger.info("[SUCCESS] 'Login' button clicked.")

    def click_remember_me_text(self) -> None:
        logger.info("[ACTION] Clicking 'Remember Me' label text...")
        self.remember_me_text.click()
        logger.info("[SUCCESS] 'Remember Me' label text clicked.")

    def check_remember_me(self) -> None:
        logger.info("[ACTION] Checking 'Remember Me' checkbox via label...")
        self.click_remember_me_text()
        logger.info("[SUCCESS] 'Remember Me' checkbox checked.")

    def click_reset_button(self) -> None:
        try:
            logger.info("[ACTION] Clicking 'Reset Email' button...")
            self.reset_pw_reset_button.click()
            logger.info("[SUCCESS] 'Reset Email' button clicked.")
        except Exception as e:
            logger.error(f"[ERROR] Failed to click 'Reset Email' button: {e}.")
            raise

    def click_cancel_button(self) -> None:
        logger.info("[ACTION] Clicking 'Cancel' button on 'Reset password' Modal...")
        self.reset_pw_cancel_button.click()
        logger.info("[SUCCESS] 'Cancel' button on 'Reset password' clicked.")

    def click_reset_password_link(self) -> None:
        logger.info("[ACTION] Clicking 'Reset Password' link...")
        self.reset_password_link.click()
        logger.info("[SUCCESS] 'Reset Password' link clicked.")

    def reset_password(self, email: str | None = None) -> None:
        if email:
            logger.info(f"[INPUT] Filling reset email: '{email}'...")
            self.reset_pw_email_input.fill(email)
            logger.info("[SUCCESS] Reset email filled.")
        else:
            logger.info("[ACTION] Resetting password with empty email field...")
        
        self.click_reset_button()
        logger.info("[SUCCESS] Password reset sequence completed.")

    def login(self, email: str, password: str) -> None:
        logger.info(f"[ACTION] Performing full login sequence for: '{email}'...")

        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        logger.info("[SUCCESS] Login sequence completed.")

    def click_signup_button(self) -> None:
        logger.info("[ACTION] Clicking 'Signup' button...")
        self.signup_button.click()
        logger.info("[SUCCESS] 'Signup' button clicked.")