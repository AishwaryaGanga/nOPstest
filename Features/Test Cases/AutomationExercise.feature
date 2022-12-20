Feature: User verifies amazon sign in page

  Scenario: Sign Up for an user
    Given Open AutomationExercise page
    When Click signup/Login link
    When Enter the details for sign_up
    Then Click Signup


  Scenario: Login to the page
    Given Open AutomationExercise page
    When Click signup/Login
    When Enter required detials
    Then Click login

  Scenario: 'Add to the cart'
    Given Open AutomationExercise page
    When Hover to dress in second row
    Then Select the product
    Then Add to the cart
    Then Verify price in cart, if it’s showing correct price or not
    Then Proceed to checkout
    Then Place the successful order

  Scenario: 'Logout from the website'
    Given Open AutomationExercise page
    Then Logout from the page

