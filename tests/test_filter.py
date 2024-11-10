"""Test the filter function of the ecommerce app"""

from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

@pytest.mark.parametrize("user", user_accounts)
def test_sort_price(user):
    """Test sorting from low to high and high to low"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # login
    login(driver, user)
    # Select Low to High filter
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")
    # Retrieve all product prices
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    # Turn the text into a float to sort the numbers later
    prices = [float(price.text.replace("$", "")) for price in prices]
    # Verify the prices are sorted in ascending order
    assert prices == sorted(prices), "Prices are not sorted from low to high"

    # Select High to Low
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (high to low)")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace("$", "")) for price in prices]
    # Verify prices in descending order
    assert prices == sorted(prices, reverse=True), "Prices are not sorted from high to low"    
    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_sort_name(user):
    """Test sorting from A to Z and Z to A"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # login
    login(driver, user)
    # Select Z to A filter
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (Z to A)")
    # Retrieve all product names
    names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [name.text for name in names]
    # Verify names are sorted in reverse
    assert names == sorted(names, reverse=True)

    # Select A to Z filter
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Name (A to Z)")
    # Retrieve all product names
    names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [name.text for name in names]
    # Verify names are sorted in reverse
    assert names == sorted(names)
    driver.quit()
