import json
import allure
import pytest
import logging
from time import time
from dataclasses import asdict
from playwright.sync_api import expect

from helpers.common_helper import mask_text
from models.data_models import CustomerLoginData
from models.data_models import CustomerSignupData
from pages.customer_login_page import CustomerLoginPage
from pages.customer_signup_page import CustomerSignupPage

logger = logging.getLogger(__name__)

@allure.parent_suite("User Management")
@allure.suite("Customer Login")
@allure.label("owner", "Mai Anh")
class TestCustomerLoginPage:
     
    @allure.sub_suite("Negative cases")
    @allure.id("TC-001")
    @allure.title("Login with an unactivated account")
    @allure.description("""
### Test Objective
Verify that the system prevents access and displays a correct warning when a user attempts to log in with an account that has not been activated via email.

### Pre-conditions
* A new account has been successfully registered.
* The account has **not** been activated (email verification link not clicked).

### Expected Results
* **Alert Visibility**: A warning alert message appears on the login page.
* **Alert Content**: The message must inform the user about the account's inactive status.
* **Security (Access Control)**: 
    * User **must not** be redirected to the Customer Dashboard.
    * The URL **must remain** on the customer login page.
""")
    @allure.tag("Login", "Activation", "Security")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.auth
    @pytest.mark.smoke
    def test_login_with_unactivated_account(
        self, 
        customer_login_page: CustomerLoginPage, 
        customer_signup_page: CustomerSignupPage
    ) -> None:
        
        logger.info("--- STARTING TEST: [TC-001] - Login with an unactivated account ---")

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

        login_user_data = CustomerLoginData(
            email=signup_user_data.email,
            password=signup_user_data.password
        )

        masked_login_data = asdict(login_user_data)
        masked_login_data["password"] = mask_text(login_user_data.password)

        allure.attach(
            json.dumps(masked_login_data, indent=4), 
            name="Data_Input_Login", 
            attachment_type=allure.attachment_type.JSON
        )

        logger.info(f"[PRE-CONDITION] Preparing signup data for: {masked_login_data}...")
        logger.debug(f"[DEBUG-DATA] [PRE-CONDITION] Preparing signup data for: {login_user_data}...")

        # Pre-requisite: Registration
        logger.info("[PRE-CONDITION] Registering unactivated account...")
        customer_signup_page.navigate()
        customer_signup_page.register_account(signup_user_data)
        logger.info("[SUCCESS] Unactivated account created.")

        # Execution Steps
        login_form = customer_login_page.login_form
        alert_card = login_form.alert_card
        not_active_account_alert_msgs = login_form.not_active_account_alert_msgs

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()
            
        with allure.step(f"Step 2: Entering email address: '{login_user_data.email}'"):
            login_form.enter_email(login_user_data.email)
            
        with allure.step("Step 3: Entering password"):
            login_form.enter_password(login_user_data.password)
            
        with allure.step("Step 4: Clicking the 'Login' button"):
            login_form.click_login_button()

        # Assertions (Validation)
        logger.info("[VERIFICATION] Verifying access block and alert messages...")

        with allure.step("Step 5: Verifying Actual Results"):
            
            with allure.step("Verifying URL remains at Customer Login page"):
                logger.info(f"[VERIFICATION] Verifying URL remains at: '{customer_login_page.URL}'...")
                expect(customer_login_page.page).to_have_url(customer_login_page.URL)
                logger.info("[SUCCESS] URL verified.")

            with allure.step("Verifying the alert card is visible"):
                logger.info("[VERIFICATION] Verifying alert card visibility...")
                expect(alert_card).to_be_visible()
                logger.info("[SUCCESS] Alert card visible.")

            with allure.step("Verifying the alert content is correct"):
                logger.info("[VERIFICATION] Verifying alert content...")
                for msg in not_active_account_alert_msgs:
                    expect(alert_card).to_contain_text(msg)
                logger.info("[SUCCESS] Alert content verified.")

        # Finalize
        logger.info("--- TEST COMPLETED: [TC-001] ---")

    @allure.sub_suite("Negative cases")
    @allure.id("TC-002")
    @allure.title("Login with non-existent credentials")
    @allure.description("""
### Test Objective
Verify that the system correctly handles login attempts with emails that are not registered in the database.

### Pre-conditions
* Use a randomly generated email to ensure it does not exist in the system.

### Expected Results
* **Alert Visibility**: An error alert message appears.
* **Alert Content**: The system displays an "Invalid Login. Please check your email and password" message.
""")
    @allure.tag("Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.auth
    def test_login_with_not_existed_account(self, customer_login_page: CustomerLoginPage) -> None:
        
        logger.info("--- STARTING TEST: [TC-002] - Login in with non-existent credentials ---")
        
        # Data Preparation
        login_user_data = CustomerLoginData(
            email=f"user_{int(time())}@gmail.com",
            password="************"
        )

        masked_login_data = asdict(login_user_data)
        masked_login_data["password"] = mask_text(login_user_data.password)

        allure.attach(
            json.dumps(masked_login_data, indent=4), 
            name="Data_Input_Login", 
            attachment_type=allure.attachment_type.JSON
        )

        logger.info(f"[PRE-CONDITION] Preparing ghost email: {masked_login_data}...")
        logger.debug(f"[DEBUG-DATA] [PRE-CONDITION] Preparing ghost email: {login_user_data}...")

        # Execution Steps
        login_form = customer_login_page.login_form
        alert_card = login_form.alert_card
        invalid_login_alert_msgs = login_form.invalid_login_alert_msgs

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()
            
        with allure.step(f"Step 2: Entering email address: '{login_user_data.email}'"):
            login_form.enter_email(login_user_data.email)
            
        with allure.step("Step 3: Entering password"):
            login_form.enter_password(login_user_data.password)
            
        with allure.step("Step 4: Clicking the 'Login' button"):
            login_form.click_login_button()

        # Assertions (Validation)
        logger.info("[VERIFICATION] Verifying invalid login response...")

        with allure.step("Step 5: Verifying Actual Results"):

            with allure.step("Verifying the alert card is visible"):
                logger.info("[VERIFICATION] Verifying alert card visibility...")
                expect(alert_card).to_be_visible()
                logger.info("[SUCCESS] Alert card visible.")

            with allure.step("Verifying the alert content is correct"):
                logger.info("[VERIFICATION] Verifying error text content...")
                for msg in invalid_login_alert_msgs:
                    expect(alert_card).to_contain_text(msg)
                logger.info("[SUCCESS] Alert content verified.")

        # Finalize
        logger.info("--- TEST COMPLETED: [TC-002] ---")

    @pytest.mark.skip(reason="Checkbox input is hidden/covered by span pseudo-element. Logic moved to TC-004.")
    @allure.sub_suite("UX cases")
    @allure.id("TC-003")
    @allure.title("'Remember me' checkbox is checkable")
    @allure.description("""
### Test Objective
Verify that the 'Remember me' checkbox element correctly accepts and maintains the 'checked' state when interacted with.

### Expected Results
* The checkbox state changes to 'checked' (selected).
* The UI reflects the checked status correctly.
""")
    @allure.tag("UX", "Login", "RememberMe")
    @allure.severity(allure.severity_level.MINOR)
    def test_remember_me_checkbox_is_checkable(self, customer_login_page: CustomerLoginPage) -> None:
        
        logger.info("--- STARTING TEST: [TC-003] - 'Remember me' checkbox is checkable ---")
        
        # Execution Steps
        login_form = customer_login_page.login_form

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()

        allure.attach(
            customer_login_page.page.screenshot(full_page=True, animations="disabled"),
            name="Screenshot_Before_Checkbox",
            attachment_type=allure.attachment_type.PNG
        )

        with allure.step("Step 2: Checking the 'Remember me' checkbox"):
            login_form.check_remember_me()

        # Assertions (Validation)
        with allure.step("Step 3: Verifying the 'Remember me' checkbox state"):
            logger.info("[VERIFICATION] Verifying the 'Remember me' checkbox state...")
            expect(login_form.remember_me_checkbox).to_be_checked()
            logger.info("[SUCCESS] 'Remember me' checkbox verified as checked.")
        
        # Finalize
        logger.info("--- TEST COMPLETED: [TC-003] ---")

    @allure.sub_suite("UX cases")
    @allure.id("TC-004")
    @allure.title("'Remember me' text is clickable")
    @allure.description("""
### Test Objective
Verify that clicking the label text 'Remember me' toggles the associated checkbox.

### Expected Results
* The checkbox should be checked when user clicks on the text label.
""")
    @allure.tag("UX", "Login", "Accessibility")
    @allure.severity(allure.severity_level.MINOR)
    def test_remember_me_text_is_clickable(self, customer_login_page: CustomerLoginPage) -> None:
        
        logger.info("--- STARTING TEST: [TC-004] - 'Remember me' text is clickable ---")
        
        # Execution Steps
        login_form = customer_login_page.login_form

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()

        allure.attach(
            customer_login_page.page.screenshot(full_page=True, animations="disabled"),
            name="Screenshot_Before_Checkbox",
            attachment_type=allure.attachment_type.PNG
        )

        with allure.step("Step 2: Clicking the 'Remember me' label text"):
            login_form.click_remember_me_text()

        # Assertions (Validation)
        with allure.step("Step 3: Verifying the 'Remember me' checkbox state"):
            logger.info("[VERIFICATION] Verifying the 'Remember me' checkbox state...")
            
            expect(login_form.remember_me_checkbox).to_be_checked()
            
            # TEST
            # expect(login_form.remember_me_text).to_be_checked()

            logger.info("[SUCCESS] 'Remember me' checkbox verified as checked.")
        
        # Finalize
        logger.info("--- TEST COMPLETED: [TC-004] ---")

    @allure.sub_suite("Negative cases")
    @allure.id("TC-005")
    @allure.title("Reset password with not existent email")
    @allure.description("""
### Test Objective
Verify the system's behavior when trying to reset a password using an email that doesn't exist.

### Expected Results
* A browser dialog (alert) should appear.
* The alert message should display the correct error notification.
""")
    @allure.tag("PasswordReset", "Modal")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.auth
    @pytest.mark.flaky
    def test_reset_password_using_not_existent_email(self, customer_login_page: CustomerLoginPage) -> None:
        
        logger.info("--- STARTING TEST: [TC-005] - Reset password with not existent email ---")
        
        # Execution Steps
        login_form = customer_login_page.login_form
        reset_email = f"user_{int(time())}@gmail.com"
        alert_info = {}

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()

        with allure.step("Step 2: Clicking the 'Reset Password' link"):
            login_form.click_reset_password_link()

            with allure.step("Waiting for 'Reset Password' modal to appear"):
                logger.info("[EVENT] Waiting for 'Reset Password' modal to become visible...")
                login_form.reset_password_modal.wait_for(state="visible")
                logger.info("[SUCCESS] 'Reset Password' modal visible.")

        allure.attach(
            customer_login_page.page.screenshot(full_page=True, animations="disabled"),
            name="Screenshot_Open_Modal",
            attachment_type=allure.attachment_type.PNG
        )

        with allure.step(f"Step 3: Processing to reset password using not existent email: '{reset_email}'"):            
            logger.info(f"[ACTION] Processing password reset for: '{reset_email}'...")
            with customer_login_page.page.expect_event("dialog") as dialog_info:
                login_form.reset_password(reset_email)
            customer_login_page.handle_browser_dialog(dialog_info.value, alert_info)
            logger.info("[SUCCESS] Password reset submitted and dialog handled.")

        # Assertions (Validation)
        with allure.step("Step 4: Verifying the alert dialog content"):
            logger.info("[VERIFICATION] Verifying the alert dialog content...")
            alert_msg = alert_info.get("message")
            assert login_form.reset_pw_invalid_email_alert_msg == alert_msg, \
                f"Expected: {login_form.reset_pw_invalid_email_alert_msg}, but got: {alert_msg}"
            logger.info("[SUCCESS] Alert content verified.")
        
        # Finalize
        logger.info("--- TEST COMPLETED: [TC-005] ---")

    @allure.sub_suite("Negative cases")
    @allure.id("TC-006")
    @allure.title("Reset password with empty email")
    @allure.description("""
### Test Objective
Verify that the system requires an email input for the password reset process.

### Expected Results
* A browser dialog (alert) should appear when attempting to reset with an empty field.
* Correct validation message is displayed.
""")
    @allure.tag("PasswordReset", "Validation", "Modal")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.auth
    @pytest.mark.flaky
    def test_reset_password_with_empty_email(self, customer_login_page: CustomerLoginPage) -> None:
        
        logger.info("--- STARTING TEST: [TC-006] - Reset password with empty email ---")
        
        # Execution Steps
        login_form = customer_login_page.login_form
        alert_info = {}

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()

        with allure.step("Step 2: Clicking the 'Reset Password' link"):
            login_form.click_reset_password_link()

            with allure.step("Waiting for 'Reset Password' modal to appear"):
                logger.info("[EVENT] Waiting for 'Reset Password' modal to become visible...")
                login_form.reset_password_modal.wait_for(state="visible")
                logger.info("[SUCCESS] 'Reset Password' modal visible.")

        with allure.step("Step 3: Processing to reset password using empty email"):
            logger.info("[ACTION] Processing password reset with empty email field...")
            customer_login_page.page.on(
                    "dialog", 
                lambda dialog: customer_login_page.handle_browser_dialog(dialog, alert_info)
            )
            login_form.reset_password()
            logger.info("[SUCCESS] Password reset submitted and dialog handled.")
            
        # Assertions (Validation)
        with allure.step("Step 4: Verifying the alert dialog content"):
            logger.info("[VERIFICATION] Verifying the alert dialog content...")
            alert_msg = alert_info.get("message")
            
            assert login_form.reset_pw_add_email_alert_msg == alert_msg, \
                f"Expected: {login_form.reset_pw_add_email_alert_msg}, but got: {alert_msg}"
            
            # TEST
            # assert login_form.not_active_account_alert_msgs == alert_msg, \
            #     f"Expected: {login_form.not_active_account_alert_msgs}, but got: {alert_msg}"
            
            logger.info("[SUCCESS] Alert content verified.")

        # Finalize
        logger.info("--- TEST COMPLETED: [TC-006] ---")

    @allure.sub_suite("UX cases")
    @allure.id("TC-007")
    @allure.title("Cancel reset password with 'Cancel' button")
    @allure.description("""
### Test Objective
Verify that the Reset Password modal can be closed using the 'Cancel' button.

### Expected Results
* The Reset Password modal should disappear from the UI.
""")
    @allure.tag("UX", "PasswordReset", "Modal")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.flaky
    def test_cancel_reset_password_with_button(self, customer_login_page: CustomerLoginPage)  -> None:
        
        logger.info("--- STARTING TEST: [TC-007] - Cancel reset password with 'Cancel' button ---")
        
        # Execution Steps
        login_form = customer_login_page.login_form

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()

        with allure.step("Step 2: Clicking the 'Reset Password' link"):
            login_form.click_reset_password_link()

            with allure.step("Waiting for 'Reset Password' modal to appear"):
                logger.info("[EVENT] Waiting for 'Reset Password' modal to become visible...")
                login_form.reset_password_modal.wait_for(state="visible")
                logger.info("[SUCCESS] 'Reset Password' modal visible.")

        allure.attach(
            customer_login_page.page.screenshot(full_page=True, animations="disabled"),
            name="Screenshot_Open_Modal",
            attachment_type=allure.attachment_type.PNG
        )

        with allure.step("Step 3: Canceling reset password using 'Cancel' button"):            
            login_form.click_cancel_button()

        # Assertions (Validation)
        with allure.step("Step 4: Verifying the 'Reset Password' modal closure"):
            logger.info("[VERIFICATION] Verifying the 'Reset Password' modal closure...")
            expect(login_form.reset_password_modal).not_to_be_visible()
            logger.info("[SUCCESS] 'Reset Password' modal verified as closed.")
        
        # Finalize
        logger.info("--- TEST COMPLETED: [TC-007] ---")
        
    @allure.sub_suite("UX cases")
    @allure.id("TC-008")
    @allure.title("Click 'Signup' button at Login page")
    @allure.description("""
### Test Objective
Verify the navigation from the Login page to the Signup page via the 'Signup' button.

### Expected Results
* User should be redirected to the correct Customer Signup URL.
""")
    @allure.tag("UX", "Navigation", "Signup")
    @allure.severity(allure.severity_level.MINOR)
    def test_signup_account_with_button_at_login_page(
        self, 
        customer_login_page: CustomerLoginPage,
        customer_signup_page: CustomerSignupPage
        ) -> None:
        
        logger.info("--- STARTING TEST: [TC-008] - Click 'Signup' button at Login page ---")
        
        # Execution Steps
        login_form = customer_login_page.login_form

        with allure.step("Step 1: Navigating to Customer Login page"):
            customer_login_page.navigate()

        with allure.step("Step 2: Clicking the 'Signup' button"):
            login_form.click_signup_button()

        # Assertions (Validation)
        with allure.step("Step 3: Verifying redirection to Customer Signup page"):
            logger.info(f"[VERIFICATION] Verifying redirection to URL: '{customer_signup_page.URL}'...")
            expect(customer_login_page.page).to_have_url(customer_signup_page.URL)
            logger.info("[SUCCESS] URL verified: Redirected to Customer signup page.")

        # Finalize
        logger.info("--- TEST COMPLETED: [TC-008] ---")

    