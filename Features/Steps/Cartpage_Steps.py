from behave import when, then


@when ('Hover to dress in second row')
def hover_to_product(context):
    context.app.cart_page.hover_to_product()

@then('Select the product')
def click_the_product(context):
    context.app.cart_page.click_the_product()

@then('Add to the cart')
def add_to_cart(context):
    context.app.cart_page.add_to_cart()

@then('Verify price in cart, if it’s showing correct price or not')
def verify_price(context):
    context.app.cart_page.verify_price()

@then('Proceed to checkout')
def check_out(context):
    context.app.cart_page.check_out()

@then('Place the successful order')
def place_order(context):
    context.app.cart_page.place_order()