from Pages.main_page import Mainpage
from Pages.Header import Header
from Pages.Sign_up_page import Open_Sign_In_Page
from Pages.Cart_Page import Hover_Action

class Application:

    def __init__(self,driver):
        self.driver = driver

        self.main_page = Mainpage(self.driver)
        self.header = Header(self.driver)
        self.sign_in = Open_Sign_In_Page(self.driver)
        self.cart_page = Hover_Action(self.driver)
