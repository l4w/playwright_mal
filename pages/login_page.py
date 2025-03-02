from playwright.sync_api import Page

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = LoginLocators()

    def go_to_login_page(self) -> None:
        self.go_to_page(path="/login.php")

    def click_on_login(self) -> None:
        self.page.click(self.locators.LOGIN_BTN)

    def fill_login_form(self) -> None:
        self.page.fill(self.locators.USERNAME, self.username)
        self.page.fill(self.locators.PASSWORD, self.password)

    def click_on_submit_login(self) -> None:
        self.page.click(self.locators.LOGIN_SUBMIT)
