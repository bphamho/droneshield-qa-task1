from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

# tests_authentication.py
# These tests are designed to test the cart functionality of the https://www.saucedemo.com application

# Test adding 1 item to cart and removing
def test_addcart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # Log into user account
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Products page

    # Add item to cart (backpack)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Verify item has been added
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart == "1"

    # Remove item from cart
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Verify item has been added
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart == "0"
    driver.quit()

# Test adding all items on the page to the cart
def test_addcartall():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Log into user account
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Find all add to cart buttons on page
    add_to_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    
    # Press each button one by one and verify cart
    for index, btn in enumerate(add_to_cart_btn):
        btn.click()
        sleep(1)
        
        # Verify cart is correct
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart == str(index + 1)
    
   
    remove_from_cart_btn = driver.find_elements(By.CSS_SELECTOR, 'button[class*="btn_inventory"]')
    
    # Remove each item one by one and verify cart
    for index, btn in enumerate(remove_from_cart_btn):
        btn.click()
        sleep(1)
        
        # Verify cart is correct
        try:
            cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            assert cart == str(len(remove_from_cart_btn) - index - 1)
        except NoSuchElementException:
            if (index != len(remove_from_cart_btn) - 1):
                raise Exception("Items added but cart badge not matching")
            pass
            
    driver.quit()