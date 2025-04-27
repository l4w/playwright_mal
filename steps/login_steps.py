import pytest_check as check

from pages.login_page import LoginPage


class LoginSteps(LoginPage):

    def verify_main_page_redirection_after_login(self) -> None:
        check.equal(
            self.page.url,
            self.base_url,
            f"Should be redirected to the main page, instead of {self.page.url}",
        )

    def verify_logged_profile_name(self) -> None:
        element = self.page.locator(self.locators.HEADER_PROFILE_LINK)
        element.is_visible()

        check.is_true(
            self.username in element.inner_text(),
            f"Env username != {element.inner_text()}",
        )

    def verify_if_logged(self) -> None:
        self.verify_logged_profile_name()
        self.verify_main_page_redirection_after_login()
