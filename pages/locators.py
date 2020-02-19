from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators(object):
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    LANG_EN_GB = (By.XPATH, '//html')
    SUCCESS_ADDITION_ALERT = (By.CSS_SELECTOR, '.alert-success')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    PRODUCT_NAME_ADDITION_ALERT = (By.CSS_SELECTOR, '.alert-success strong')


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators(object):
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.content div#content_inner p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items .row")


