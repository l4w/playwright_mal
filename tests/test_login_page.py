import pytest
from playwright.sync_api import Page
from steps.login_steps import LoginSteps


class TestLoginPage:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_steps = LoginSteps(page)

    def test_login_from_main_page(self):
        self.login_steps.go_to_page()
        self.login_steps.click_on_login()
        self.login_steps.fill_login_form()
        self.login_steps.click_on_submit_login()

        self.login_steps.verify_if_logged()
