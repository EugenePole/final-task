from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import math


class ProductPage(BasePage):
    def add_product_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_BUTTON), "Add to cart button is not presented on Product page"
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def alert_success_addition_present(self):
        success_addition_phrase_en_gb = 'has been added to your basket'
        assert 'en-gb' == self.browser.find_element(*ProductPageLocators.LANG_EN_GB).get_attribute(
            'lang'), "Current page language is not 'en-gb'"
        assert success_addition_phrase_en_gb in self.browser.find_elements(*ProductPageLocators.SUCCESS_ADDITION_ALERT)[
            0].text, \
            'success addition alert not contain phrase "{}"'.format(success_addition_phrase_en_gb)

    def equal_product_name_and_added_product(self, product_name=None):
        product_name_in_success_alert = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_ADDITION_ALERT)[
            0].text
        assert product_name == product_name_in_success_alert, 'choosen: "{}" not equal added: "{}"'.format(product_name,
                                                                                                           product_name_in_success_alert)

    def click_to_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'product page no add to cart button presented'
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_ADDITION_ALERT), 'Success message is presented, but should not be'

    def should_be_disappeared_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_ADDITION_ALERT), 'Success message is presented, but should not be'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
