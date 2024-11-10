# TEST-STRATEGY

## 1. Test Objective
The objective of this task is to verify the functionality, performance and reliability of the https://www.saucedemo.com/ web application

## 2. Test Approach
- The test strategy for this task would be to use an automated testing approach with Selenium to verify the core user interactions.
- Manual testing will also be performend as way of familiarising with the functionality of this website and to identify any issues.
- The core functionality of this website will be focused on with the users provided.

## 3. Types of Testing
- Functional testing: Ensuring the functionality of the web application operates as expected
- Performance testing: Observe response time of the web application
- UI testing: Ensure UI elements are rendered correctly and as expected.

## 4. Testing Tools:
- elenium WebDriver: To simulate user actions and verify UI functionality.
- Pytest: As the test framework to handle parameterized tests for different user accounts.

# TEST-PLAN

## Test Cases

1. Authentication Validation:
- Verify the lists of users provided can log in and out.

2. Product Page Validation:
- Verify that the each product's name, description and price remain consistent throughout the web application.

3. Shopping Cart Validation:
- Verify that items added to cart are displayed correctly and as expected.

4. Checkout Validation
- Verify that when using the checkout functionality that all the items that are added to the cart are ordered succesfully.

## Risks
- Testing is currently only performed on a desktop environment so no mobile testing is performed.

# DECISIONS AND REASONS
1. Automated Testing
- Decision: Use of automated testing with the Selenium Framework with Python and pytest
- Reasons: Allows for testing of repetitive actions and coverage of the multiple users provided

2. Repeating each test case for all users
- Decision: Run each test case for each individual user provided on the web application
- Reason: Each user (apart from standard_user) has bugs related to them so testing all test cases for each one will allow for bug discovery.

3. Manual Testing
- Decision: Use of manual testing
- Reason: To explore functionality that may not be noticed just through automation