from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "No 'login' in url of the Login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Register form isn't presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2).send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), "User icon is not presented," \
                                                                      " probably unauthorised user"

