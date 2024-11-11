"""Test the checkout functionality of the https://www.saucedemo.com application"""

from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

user_accounts = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "problem_user", "password": "secret_sauce"},
    {"username": "performance_glitch_user", "password": "secret_sauce"},
    {"username": "error_user", "password": "secret_sauce"},
    {"username": "visual_user", "password": "secret_sauce"},
]

def login(driver, user):
    """Function to perform login"""

    # Log into user account
    driver.find_element(By.ID, "user-name").send_keys(user["username"])
    driver.find_element(By.ID, "password").send_keys(user["password"])
    driver.find_element(By.ID, "login-button").click()

def add_item_to_cart(driver, item_name):
    """Function to add item to cart and store details"""
    item = driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']")
    item.find_element(By.CLASS_NAME, "btn_inventory").click()
    price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
    # Track item details in a dictionary
    return {item_name: {"price": price, "quantity": 1}}

def get_checkout_items(driver):
    """Function to get details of items in checkout"""
    checkout_items = {}
    checkout_products = driver.find_elements(By.CLASS_NAME, "cart_item")

    # Extract details for each item in the checkout
    for item in checkout_products:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        quantity = item.find_element(By.CLASS_NAME, "cart_quantity").text
        # Add each item to the dictionary
        checkout_items[name] = {
            "price": price,
            "quantity": int(quantity)
        }

    return checkout_items

@pytest.mark.parametrize("user", user_accounts)
def test_checkout(user):
    """Perform checkout with 1 item"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)

    # Initialize a dictionary to store added items
    added_items = {}
    # Add an example item to the cart and store its details
    added_items.update(add_item_to_cart(driver, "Sauce Labs Backpack"))
    print(added_items)

    # Click on cart top right
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Click on checkout button
    driver.find_element(By.NAME, "checkout").click()

    sleep(1)
    # Enter in details
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("2000")

    # Press Continue
    driver.find_element(By.ID, "continue").click()

    # Verify product
    checkout_items = get_checkout_items(driver)
    print(checkout_items)

    assert added_items == checkout_items,  "Items in checkout do not match items added to the cart."
    # Press Finish
    driver.find_element(By.ID, "finish").click()

    # Verify order was purchased
    header = driver.find_element(By.CLASS_NAME, "complete-header").text

    assert header == "Thank you for your order!"

    # Press Back Home button
    driver.find_element(By.ID, "back-to-products").click()

    # Verify page is products page
    header = driver.find_element(By.CLASS_NAME, "title").text
    assert header == "Products"

    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_checkout_mutliple(user):
    """Perform checkout with all items"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)

    # Find all add to cart buttons on page
    add_to_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    # Press each button one by one and verify cart
    for btn in add_to_cart_btn:
        btn.click()
    # Checkout
    # Click on cart top right
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Click on checkout button
    driver.find_element(By.NAME, "checkout").click()

    sleep(1)
    # Enter in details
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("2000")

    # Press Continue
    driver.find_element(By.ID, "continue").click()

    # Verify products in checkout


    # Press Finish
    driver.find_element(By.ID, "finish").click()

    # Verify order was purchased
    header = driver.find_element(By.CLASS_NAME, "complete-header").text

    assert header == "Thank you for your order!"

    # Press Back Home button
    driver.find_element(By.ID, "back-to-products").click()

    # Verify page is products page
    header = driver.find_element(By.CLASS_NAME, "title").text
    assert header == "Products"

    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_repeat_checkout(user):
    """Repeat checkout with same item and details"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)
    for _ in range(2):
        # Add first item to cart
        driver.find_element(By.CSS_SELECTOR, 'button[class*="btn_inventory"]').click()

        # Click on cart top right
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Click on checkout button
        driver.find_element(By.NAME, "checkout").click()

        sleep(1)
        # Enter in details
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("2000")

        # Press Continue
        driver.find_element(By.ID, "continue").click()

        sleep(1)
        # Press Finish
        driver.find_element(By.ID, "finish").click()

        # Verify order was purchased
        header = driver.find_element(By.CLASS_NAME, "complete-header").text

        sleep(2)
        assert header == "Thank you for your order!"

        # Press Back Home button
        driver.find_element(By.ID, "back-to-products").click()
        sleep(2)
        # Verify page is products page
        header = driver.find_element(By.CLASS_NAME, "title").text
        assert header == "Products"

    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_repeat_checkout(user):
    """Test checkout total matches with prices of total prices of items and tax is calculated correctly"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login(driver,user)
    
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    expected_subtotal = 0.0
    
    # Add items to cart and keep track of total
    for item in items:
        # Get item price
        price_text = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        price = float(price_text.replace("$", ""))
        
        # Add price to expected total
        expected_subtotal += price
        
        # Add the item to the cart
        item.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # Go to checkout
    driver.find_element(By.ID, "checkout").click()
    
    # Enter in details
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("2000")
    driver.find_element(By.ID, "continue").click()
    
    # Get the displayed subtotal, tax, and total from the checkout overview page
    subtotal_text = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    tax_text = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text    

    # Get the values from text
    displayed_subtotal = float(subtotal_text.replace("Item total: $", ""))
    displayed_tax = float(tax_text.replace("Tax: $", ""))
    displayed_total = float(total_text.replace("Total: $", ""))
    
    # Add tax to expected total
    expected_total = expected_subtotal + displayed_tax

    # Get the total price displayed on the checkout overview page
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    displayed_total = float(total_text.replace("Total: $", ""))

    # Verify that the displayed subtotal matches the expected subtotal
    assert expected_subtotal == displayed_subtotal, f"Subtotal mismatch: expected ${expected_subtotal}, but got ${displayed_subtotal}"

    # Verify that the expected total (subtotal + tax) matches the displayed total
    assert expected_total == displayed_total, f"Cart total mismatch: expected ${expected_total}, but got ${displayed_total}"

    driver.quit()
    