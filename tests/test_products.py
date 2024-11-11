"""Test the product functionality of the commerce app"""
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

def get_product_details_from_page(product_element):
    """Function to get product details from the all products page"""
    # Extract product name and price from the products page
    product_name = product_element.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = product_element.find_element(By.CLASS_NAME, "inventory_item_price").text
    return product_name, product_price

def get_product_details_after_click(driver, product_element):
    """Function to get product details from the products detail page"""
    product_link = product_element.find_element(By.TAG_NAME, "a")
    product_link.click()  # Click on the product to open its details
    # If the website uses a modal, you would extract details from the modal
    product_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
    product_price = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
    return product_name, product_price

@pytest.mark.parametrize("user", user_accounts)
def test_products_details(user):
    """Test to check if the product on the products page matches with the item details"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Log in
    login(driver, user)

    # Get all products on the page
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # Click on each product and compare to the product description in the products page
    length = len(products)
    for i in range(length):
        # Get product details from the products page
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        product_name_on_page, product_price_on_page = get_product_details_from_page(products[i])

        # Get product details after clicking on the product
        product_name_after_click, product_price_after_click = get_product_details_after_click(driver, products[i])

        # Assertions to verify if the product details match
        assert product_name_on_page == product_name_after_click, f"Product names do not match for product {i + 1}: '{product_name_on_page}' != '{product_name_after_click}'"
        assert product_price_on_page == product_price_after_click, f"Product prices do not match for product {i + 1}: '{product_price_on_page}' != '{product_price_after_click}'"
        print(f"Product {i + 1} passed: {product_name_on_page} | Price: {product_price_on_page}")
        # Navigate back to the products page

        driver.back()

    driver.quit()
