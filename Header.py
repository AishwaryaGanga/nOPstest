from Pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SIGNUP_LOGIN =(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    LOGOUT =(By.CSS_SELECTOR, "[href='/logout']")

    def go_to_sign_up_page(self):
        self.click(*self.SIGNUP_LOGIN)

    def log_out(self):
        self.click(*self.LOGOUT)