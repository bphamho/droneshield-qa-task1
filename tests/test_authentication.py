"""Test the authentication function of the ecommerce app"""

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
    {"username": "locked_out_user", "password": "secret_sauce"},
]

def test_page_load():
    """Test to make sure page loads"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs", "Website did not load or incorrect website"
    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_logins(user):
    """Test User logins and logout
    users: standard_user, problem_user, performance_glitch_user, error_user, visual_user
    passwords: secret_sauce"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Initialize user lists and password

    # Recursive logging in, logging out, then sign into next user
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    # Enter in username and password
    driver.find_element(By.ID, "user-name").send_keys(user["username"])
    driver.find_element(By.ID, "password").send_keys(user["password"])
    # Press login button
    driver.find_element(By.ID, "login-button").click()
    # Verify that user is loggedin

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" == title, "Incorrect page"
    # Log out
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, "Logout").click()


    driver.quit()

@pytest.mark.parametrize("user", user_accounts)
def test_fail_login_user(user):
    """Test fail login with correct usernames and incorrect password"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Enter in username and password
    driver.find_element(By.ID, "user-name").send_keys(user["username"])
    driver.find_element(By.ID, "password").send_keys("test123")
    # Press login button
    driver.find_element(By.ID, "login-button").click()  
    # Verify user is incorrect
    error = driver.find_element("xpath", '//*[@data-test="error"]')
    assert error, "Login was successful (failed test case)"

    driver.quit()

def test_fail_login_password():
    """Test fail login with incorrect username and incorrect password"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Enter in username and password
    driver.find_element(By.ID, "user-name").send_keys("test123")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # Press login button
    driver.find_element(By.ID, "login-button").click()
    # Verify user is incorrect
    error = driver.find_element("xpath", '//*[@data-test="error"]')
    assert error, "Login was successful (failed test case)"

    driver.quit()

def test_empty_username():
    """Test empty password"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Empty username
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # Press login button
    driver.find_element(By.ID, "login-button").click()
    # Verify user is incorrect
    error = driver.find_element("xpath", '//*[@data-test="error"]')
    assert error.text == "Epic sadface: Username is required", "Username field was not empty"

    driver.quit()

def test_empty_password():
    """Test empty password"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    #Empty password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    # Press login button
    driver.find_element(By.ID, "login-button").click()
    # Verify user is incorrect
    error = driver.find_element("xpath", '//*[@data-test="error"]')
    assert error.text == "Epic sadface: Password is required", "Password field was not empty"

    driver.quit()
