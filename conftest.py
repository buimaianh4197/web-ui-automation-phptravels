import allure
import pytest
import logging
from pathlib import Path
from typing import Generator
from _pytest.nodes import Item
from playwright.sync_api import Page

from pages.signup_success_page import SignupSuccessPage
from pages.customer_login_page import CustomerLoginPage
from pages.customer_signup_page import CustomerSignupPage

logger = logging.getLogger(__name__)

@pytest.fixture()
def customer_signup_page(page: Page):
    logger.debug("[CONFIG] Initializing CustomerSignupPage fixture")
    yield CustomerSignupPage(page)

@pytest.fixture()
def signup_success_page(page: Page):
    logger.debug("[CONFIG] Initializing SignupSuccessPage fixture")
    yield SignupSuccessPage(page)

@pytest.fixture()
def customer_login_page(page: Page):
    logger.debug("[CONFIG] Initializing CustomerLoginPage fixture")
    yield CustomerLoginPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: pytest.CallInfo) -> Generator:
    outcome = yield
    report = outcome.get_result()

    page = None
    funcargs = getattr(item, "funcargs", {})
    if "page" in funcargs:
        page = funcargs["page"]
    else:
        for fixture_value in funcargs.values():
            if hasattr(fixture_value, "page") and isinstance(fixture_value.page, Page):
                page = fixture_value.page
                break
    
    if not page:
        logger.debug(f"[DEBUG] No Playwright page object found for test: {item.name}")

    if report.when == "call":
        item.test_failed = report.failed
        status = "PASSED" if report.passed else "FAILED"
        
        if report.passed:
            logger.info(f"[EVENT] --- TEST PASSED: {item.name} ---")
        else:
            logger.error(f"[EVENT] --- TEST FAILED: {item.name} ---")
            
            if hasattr(report.longrepr, "reprcrash"):
                msg = f"{report.longrepr.reprcrash.message} (at {report.longrepr.reprcrash.path}:{report.longrepr.reprcrash.lineno})"
            else:
                msg = str(report.longrepr)

            logger.error(f"[ERROR] Reason: {msg}")

        if page:
            try:
                logger.info(f"[ACTION] Capturing {status} screenshot...")
                allure.attach(
                    page.screenshot(full_page=True, animations="disabled"),
                    name=f"Screenshot_{status}_Call",
                    attachment_type=allure.attachment_type.PNG
                )
                logger.info(f"[SUCCESS] Screenshot attached to Allure")
            except Exception as e:
                logger.warning(f"[WARNING] Could not capture screenshot: {e}")

    if report.when == "teardown":
        is_failed = getattr(item, "test_failed", False)
        
        if is_failed:
            logger.info(f"[ACTION] Test FAILED. Searching for Trace and Video artifacts...")
            
            output_dir = Path(item.config.getoption("--output") or "test-results")
            if not output_dir.exists():
                logger.error(f"[ERROR] Artifacts directory not found: {output_dir}")
                return

            test_method_name = item.name.split('[')[0]
            found_folder = False

            for entry in output_dir.iterdir():
                if entry.is_dir() and test_method_name in entry.name.replace("-", "_"):
                    found_folder = True
                    logger.debug(f"[DEBUG] Matching artifact folder found: {entry.name}")
                    
                    trace_file = entry / "trace.zip"
                    if trace_file.exists():
                        logger.info(f"[ATTACH] Attaching Trace file: {trace_file}")
                        allure.attach.file(str(trace_file), name="Log_Error_Trace", attachment_type=allure.attachment_type.ZIP)
                    else:
                        logger.debug(f"[DEBUG] Trace file not found in {entry}")

                    video_file = entry / "video.webm"
                    if video_file.exists():
                        logger.info(f"[ATTACH] Attaching Video file: {video_file}")
                        allure.attach.file(str(video_file), name="Log_Error_Video", attachment_type=allure.attachment_type.WEBM)
                    else:
                        logger.debug(f"[DEBUG] Video file not found in {entry}")
            
            if not found_folder:
                logger.warning(f"[WARNING] No artifact folder found for test: {test_method_name}")
        else:
            logger.info(f"[EVENT] Test PASSED. Skipping Trace and Video attachments.")