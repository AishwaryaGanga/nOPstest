from selenium.webdriver.common.by import By
from Pages.base_page import Page


class Open_Sign_In_Page(Page):
    SIGN_UP = (By.CSS_SELECTOR, "Click signup/Login link")
    NAME = (By.XPATH, "//input[@name='name']")
    PASSWORD = (By.CSS_SELECTOR, '[type="password"]')
    EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[type='submit'][data-qa='signup-button'].btn.btn-default")
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-qa="login-button"]')

    def sign_up(self):
        self.click(*self.SIGN_UP)

    def sign_up_details(self):
        self.input_text('John Doe', *self.NAME)
        self.input_text('johndoe@gmail.com', *self.EMAIL)

    def login_details(self):
        self.input_text('johndoe@gmail.com', *self.EMAIL)
        self.input_text('password',self.PASSWORD)

    def click_Login_btn(self):
        self.click(*self.LOGIN_BTN)


    def click_Signup_btn(self):
        self.click(*self.SIGNUP_BTN)