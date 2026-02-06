import json
import allure
import pytest
import logging
from time import time
from dataclasses import asdict
from playwright.sync_api import expect

from helpers.common_helper import mask_text
from models.data_models import CustomerSignupData
from pages.signup_success_page import SignupSuccessPage
from pages.customer_signup_page import CustomerSignupPage

logger = logging.getLogger(__name__)

@allure.parent_suite("User Management")
@allure.suite("Customer Signup")
@allure.label("owner", "Mai Anh")
class TestCustomerSignupPage:
     
    @allure.sub_suite("Positive cases")
    @allure.id("TC-001")
    @allure.title("Successful signup form submission")
    @allure.description("""
### Test Objective
Verify that a new customer can successfully submit the signup form using valid credentials.

### Pre-conditions
* User is on the Signup page.

### Expected Results
* **Redirection**: System redirects to url: `https://www.phptravels.net/signup_success`.
* **Notification**: A success message is displayed: *"Your account has been created. Please check your mailbox for activation"*
""")
    @allure.tag("Signup")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.auth
    @pytest.mark.smoke
    def test_signup_form_submission_success(self, customer_signup_page: CustomerSignupPage, signup_success_page: SignupSuccessPage):
        
        logger.info("--- STARTING TEST: [TC-001] - Successful signup form submission ---")

        # Data Preparation
        signup_user_data = CustomerSignupData(
            first_name="Ha Lan",
            last_name="Nguyen",
            country="Viet Nam",
            phone="0987356278",
            email=f"user_{int(time())}@gmail.com",
            password="************"
        )

        masked_signup_data = asdict(signup_user_data)
        masked_signup_data["password"] = mask_text(signup_user_data.password)

        allure.attach(
            json.dumps(masked_signup_data, indent=4), 
            name="Data_Input_Signup", 
            attachment_type=allure.attachment_type.JSON
        )

        logger.info(f"[PRE-CONDITION] Preparing signup data for: '{masked_signup_data}'...")
        logger.debug(f"[DEBUG-DATA] [PRE-CONDITION] Preparing signup data for: '{signup_user_data}'...")

        # Execution Steps
        with allure.step("Step 1: Navigating to Customer Signup page"):
            customer_signup_page.navigate()

        with allure.step(f"Step 2: Entering first name: '{signup_user_data.first_name}'"):
            customer_signup_page.enter_first_name(signup_user_data.first_name)
            
        with allure.step(f"Step 3: Entering last name: '{signup_user_data.last_name}'"):
            customer_signup_page.enter_last_name(signup_user_data.last_name)
            
        with allure.step(f"Step 4: Selecting country: '{signup_user_data.country}'"):
            customer_signup_page.select_country(signup_user_data.country)
            
        with allure.step(f"Step 5: Entering phone number: '{signup_user_data.phone}'"):
            customer_signup_page.enter_phone(signup_user_data.phone)
            
        with allure.step(f"Step 6: Entering email address: '{signup_user_data.email}'"):
            customer_signup_page.enter_email(signup_user_data.email)
            
        with allure.step("Step 7: Entering password"):
            customer_signup_page.enter_password(signup_user_data.password)

        with allure.step("Step 8: Clicking captcha checkbox"):
            customer_signup_page.click_captcha_checkbox()
            
        with allure.step("Step 9: Solving captcha challenge"):
            customer_signup_page.wait_for_solve_captcha()
            
        with allure.step("Step 10: Clicking the 'Signup' button"):
            customer_signup_page.click_signup_button()

        # Assertions (Validation)
        logger.info("[VERIFICATION] Verifying signup success redirection and messages...")

        with allure.step("Step 11: Verifying Actual Results"):
            with allure.step("Verifying redirection to the Success Page"):
                logger.info(f"[VERIFICATION] Verifying redirection to URL: '{signup_success_page.URL}'...")
                expect(customer_signup_page.page).to_have_url(signup_success_page.URL)
                logger.info("[SUCCESS] URL verified.")
            
            with allure.step("Verifying the activate account notification card is visible"):
                logger.info("[VERIFICATION] Verifying notification card visibility...")
                expect(signup_success_page.notification_card).to_be_visible()
                logger.info("[SUCCESS] Notification card visible.")
            
            with allure.step("Verifying the activate account notification content"):
                logger.info("[VERIFICATION] Verifying notification text content...")
                for msg in signup_success_page.activate_account_mgs:
                    expect(signup_success_page.notification_card).to_contain_text(msg)
                logger.info("[SUCCESS] Notification content verified.")

        # Finalize
        logger.info("--- TEST COMPLETED: [TC-001] ---")