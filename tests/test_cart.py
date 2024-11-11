"""Test the cart functionality of the commerce app"""

from time import sleep
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

@pytest.mark.parametrize("user", user_accounts)
def test_addcart(user):
    """Test adding 1 item to cart and removing"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Log into user account
    login(driver, user)

    # Products page

    # Add item to cart (backpack)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Verify item has been added
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart == "1", "Cart number incorrect"

    # Remove item from cart
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Verify item has been added
    try:
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        raise ValueError("Still an item in the cart")
    except NoSuchElementException:
        pass

@pytest.mark.parametrize("user", user_accounts)
def test_addcartall(user):
    """Test adding all items on the page to the cart and then removing"""

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)

    # Find all add to cart buttons on page
    add_to_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    # Press each button one by one and verify cart
    for index, btn in enumerate(add_to_cart_btn):
        btn.click()
        # Verify cart is correct
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart == str(index + 1), "Cart number incorrect"
    remove_from_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    # Remove each item one by one and verify cart
    for index, btn in enumerate(remove_from_cart_btn):
        btn.click()
        # Verify cart is correct
        try:
            cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            assert cart == str(len(remove_from_cart_btn) - index - 1), "Cart number incorrect"
        except NoSuchElementException as exc:
            if index != len(remove_from_cart_btn) - 1:
                raise ValueError("Items added but cart badge not matching") from exc
    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_remove_from_cart(user):
    """Test removing items from cart"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)

    # Find all add to cart buttons on page
    add_to_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    # Press each button one by one and verify cart
    for index, btn in enumerate(add_to_cart_btn):
        btn.click()
        # Verify cart is correct
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart == str(index + 1), "Cart number incorrect"
    # Click on cart top right
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # Remove each item one by one and verify cart
    remove_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="cart_button"]')
    for index, btn in enumerate(remove_btn):
        btn.click()
        sleep(1)
        # Verify cart is correct
        try:
            cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            assert cart == str(len(remove_btn) - index - 1), "Cart number incorrect"
        except NoSuchElementException as exc:
            if index != len(remove_btn) - 1:
                raise ValueError("Items added but cart badge not matching") from exc
    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_verify_items_in_cart(user):
    """Test to verify items added are in cart"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)

    # Create added items dictionary and add the items to the cart
    added_items = {}
    added_items.update(add_item_to_cart(driver, "Sauce Labs Backpack"))
    added_items.update(add_item_to_cart(driver, "Sauce Labs Bike Light"))
    added_items.update(add_item_to_cart(driver, "Sauce Labs Bolt T-Shirt"))
    added_items.update(add_item_to_cart(driver, "Sauce Labs Fleece Jacket"))
    added_items.update(add_item_to_cart(driver, "Sauce Labs Onesie"))
    added_items.update(add_item_to_cart(driver, "Test.allTheThings() T-Shirt (Red)"))

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify the items in the cart match with the items added
    cart_items = {}

    # Locate all items in the cart
    cart_products = driver.find_elements(By.CLASS_NAME, "cart_item")
    # Extract details for each item in the cart
    for item in cart_products:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        quantity = item.find_element(By.CLASS_NAME, "cart_quantity").text

        # Store item details in a dictionary
        cart_items[name] = {
            "price": price,
            "quantity": int(quantity)
        }

    assert added_items == cart_items, "Items in cart don't match with added items"

@pytest.mark.parametrize("user", user_accounts)
def test_user_logout(user):
    """Test cart when user logs out"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    login(driver, user)

    # Find all add to cart buttons on page
    add_to_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    # Press each button one by one and verify cart
    for index, btn in enumerate(add_to_cart_btn):
        btn.click()
        # Verify cart is correct
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart == str(index + 1), "Cart number incorrect"
    # Log out
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, "Logout").click()

    # Log back in
    login(driver, user)

    # Check cart size is correct
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart == str(len(add_to_cart_btn)), "Cart number incorrect"

    driver.quit()
