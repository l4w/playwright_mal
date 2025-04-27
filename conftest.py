import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from steps.login_steps import LoginSteps


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context: BrowserContext = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    context_page: Page = context.new_page()
    yield context_page
    context_page.close()


@pytest.fixture(scope="function")
def login(page):
    login_steps = LoginSteps(page)

    login_steps.go_to_page()
    login_steps.click_on_login()
    login_steps.fill_login_form()
    login_steps.click_on_submit_login()

    login_steps.verify_if_logged()
