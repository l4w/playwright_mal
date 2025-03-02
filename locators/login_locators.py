from locators.base_locators import BaseLocators


class LoginLocators(BaseLocators):
    LOGIN_BTN = "#malLogin"
    USERNAME = "#loginUserName"
    PASSWORD = "#login-password"
    LOGIN_SUBMIT = "input[type='submit'][value='Login']"
    HEADER_PROFILE_LINK = ".header-profile-link"
