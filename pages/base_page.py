import os

from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.username, self.password = os.getenv("LOGIN"), os.getenv("PASSWORD")

    def go_to_page(self, path: str = ""):
        """
        Navigates to the stated path on the website, goes to the base page by default
        """
        self.page.goto(self.base_url + path)
