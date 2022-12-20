from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open AutomationExercise page')
def open_automationexercise_page(context):
    context.app.main_page.open_automationexercise_page()

@when('Click signup/Login link')
def go_to_sign_up_page(context):
    context.app.sign_in.go_to_sign_up_page()

@when('Enter the details for sign_up')
def sign_up_details(context):
    context.app.sign_in.sign_up_details()

@then('Click Signup')
def click_Signup_btn(context):
    context.app.sign_in.click_Signup_btn()