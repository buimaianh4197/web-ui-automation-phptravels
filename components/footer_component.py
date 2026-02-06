import logging
from playwright.sync_api import Page, Locator

logger = logging.getLogger(__name__)

class FooterComponent:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.root = self.page.locator("section.footer-area")

        self.about_us_link = self.root.get_by_role("link", name="About Us")
        self.privacy_policy_link = self.root.get_by_role("link", name="Privacy Policy")
        self.file_a_claim_link = self.root.get_by_role("link", name="File A Claim")
        self.contact_us_link = self.root.locator("ul.dropdown-menu-item").get_by_role("link", name="Contact Us")
        self.become_a_supplier_link = self.root.get_by_role("link", name="Become A Supplier")
        self.careers_and_jobs_link = self.root.get_by_role("link", name="Careers And Jobs")
        self.faq_link = self.root.get_by_role("link", name="Faq")
        self.how_to_book_link = self.root.get_by_role("link", name="How To Book")
        self.terms_of_use_link = self.root.get_by_role("link", name="Terms Of Use")
        self.cookies_policy_link = self.root.get_by_role("link", name="Cookies Policy")
        self.booking_tips_link = self.root.get_by_role("link", name="Booking Tips")

        self.agency_logo = self.root.get_by_role("link", name="logo")
        self.phone = self.root.get_by_text("+123456789")
        self.email = self.root.get_by_text("email@agency.com")
        self.contact_icon = self.root.locator("ul.list-items").get_by_role("link", name="Contact Us")

        self.newsletter_name_input = self.root.locator("input[name='name']")
        self.newsletter_email_input = self.root.locator("input[name='email']")
        self.subscribe_button = self.root.get_by_role("button", name="Signup Newsletter")

        self.copyright = self.root.get_by_text("All Rights Reserved by PHPTARVELS")
        self.powered_by = self.root.get_by_text("Powered by PHPTRAVELS v9.1")
        self.platform_logo = self.root.get_by_role("link", name="phptravels")

        self.facebook_icon = self.root.locator('ul.social-profile a[href="https://facebook.com/phptravels"]')
        self.twitter_icon = self.root.locator('ul.social-profile a[href="https://twitter.com/phptravelss"]')
        self.linkedin_icon = self.root.locator('ul.social-profile a[href="https://twitter.com/phptravels"]')
        self.google_plus_icon = self.root.locator('ul.social-profile a[href="https://google.com/phptravels"]')
        self.youtube_icon = self.root.locator('ul.social-profile a[href="https://youtube.com/phptravels"]')
        self.whatsapp_icon = self.root.locator('ul.social-profile a[href="https://whatsapp.com/phptravels"]')
        self.instagram_icon = self.root.locator('ul.social-profile a[href="https://instagram.com/phptravels"]')

    def click_footer_link(self, link_locator: Locator) -> None:
        logger.info(f"[ACTION] Clicking on footer link: {link_locator}...")
        link_locator.click()
        logger.info(f"[SUCCESS] {link_locator} clicked.")

    def click_social_icon(self, social_icon_locator: Locator) -> None:
        logger.info(f"[ACTION] Navigating to social media profile: {social_icon_locator}...")
        social_icon_locator.click()
        logger.info(f"[SUCCESS] {social_icon_locator} navigation completed.")

    def click_agency_logo(self) -> None:
        logger.info("[ACTION] Clicking 'Agency Logo' in footer...")
        self.agency_logo.click()
        logger.info("[SUCCESS] 'Agency Logo' clicked.")

    def click_platform_logo(self) -> None:
        logger.info("[ACTION] Clicking 'PHPTRAVELS' platform logo...")
        self.platform_logo.click()
        logger.info("[SUCCESS] 'PHPTRAVELS' platform logo clicked.")

    def click_contact_link(self) -> None:
        logger.info("[ACTION] Clicking 'Contact Us' info link in footer...")
        self.contact_icon.click()
        logger.info("[SUCCESS] 'Contact Us' info link clicked.")

    def enter_name(self, name: str) -> None:
        logger.info(f"[INPUT] Entering name for newsletter: '{name}'...")
        self.newsletter_name_input.fill(name)
        logger.info("[SUCCESS] Name entered.")

    def enter_email(self, email: str) -> None:
        logger.info(f"[INPUT] Entering email for newsletter: '{email}'...")
        self.newsletter_email_input.fill(email)
        logger.info("[SUCCESS] Email entered.")

    def click_subscribe_button(self) -> None:
        logger.info("[ACTION] Clicking 'Signup' button on Newsletter form...")
        self.subscribe_button.click()
        logger.info("[SUCCESS] 'Signup' button clicked.")

    def subscribe_newsletter(self, name: str, email: str) -> None:
        logger.info(f"[ACTION] Performing full newsletter subscription for: '{email}'...")

        self.enter_name(name)
        self.enter_email(email)
        self.click_subscribe_button()
        
        logger.info("[SUCCESS] Newsletter subscription form submitted.")