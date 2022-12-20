from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep

class Hover_Action(Page):
    HOVER_TO_PRODUCT = (By.CSS_SELECTOR," div.col-sm-4:nth-child(6) div.product-image-wrapper div.single-products")
    CLICK_THE_PRODUCT = (By.CSS_SELECTOR,"[href='/product_details/4']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[type='button']")
    VIEW_CART = (By.XPATH, "//u[normalize-space()='View Cart']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".cart_total_price")
    CHECKOUT = (By.CSS_SELECTOR, ".btn.btn-default.check_out")
    PLACE_ORDER= (By.CSS_SELECTOR, "[href='/payment']")

    def hover_to_product(self):
        product = self.find_element(*self.HOVER_TO_PRODUCT)
        actions = ActionChains(self.driver)
        actions.move_to_element(product)
        actions.perform()
        sleep(5)

    def click_the_product(self):
        self.click(*self.CLICK_THE_PRODUCT)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)
        self.click(*self.VIEW_CART)


    def verify_price(self):
        expected_text = 'Rs. 1500'
        actual_text = self.find_element(*self.PRODUCT_PRICE).text
        assert actual_text == expected_text, f'Expected{expected_text} but got {actual_text}'

    def check_out(self):
        self.click(*self.CHECKOUT)

    def place_order(self):
        self.click(*self.PLACE_ORDER)

