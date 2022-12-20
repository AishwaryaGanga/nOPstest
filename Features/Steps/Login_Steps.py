from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click signup/Login')
def go_to_sign_up_page(context):
    context.app.header.go_to_sign_up_page()

@when('Enter required detials')
def login_details(context):
    context.app.sign_in.login_details()

@then('Click login')
def click_Login_btn(context):
    context.app.sign_in.click_Login_btn()