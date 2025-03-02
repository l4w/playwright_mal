import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


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
