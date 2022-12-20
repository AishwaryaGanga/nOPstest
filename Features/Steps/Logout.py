from behave import then

@then('Logout from the page')
def log_out(context):
    context.app.header.log_out()