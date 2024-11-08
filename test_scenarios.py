from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
from time import sleep

# Test to make sure page loads
def test_page_load():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"
    driver.quit()
    
# Test User logins and logout
# users:
# standard_user
# problem_user
# performance_glitch_user
# error_user
# visual_user
# passwords:
# secret_sauce
def test_logins():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # Initialize user lists and password
    users = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
    password = "secret_sauce"
    
    
    # Recursive logging in, logging out, then sign into next user
    
    for user in users:
        # Enter in username and password
        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.ID, "password").send_keys(password)
        
        # Press login button
        driver.find_element(By.ID, "login-button").click()
        
        sleep(5)
        # Verify that user is loggedin
        title = driver.find_element(By.CLASS_NAME, "title").text
        assert "Products" == title
        
        # Log out
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        sleep(1)
        driver.find_element(By.LINK_TEXT, "Logout").click()
    
    driver.quit()
    
# Test incorrect password and username
def fail_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # Test 1: Correct username, incorrect password
    users = ["standard_user", "locked_out_user","problem_user", "performance_glitch_user", "error_user", "visual_user"]
    
    
    # Recursive logging in, logging out, then sign into next user
    
    for user in users:
        # Enter in username and password
        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.ID, "password").send_keys("test123")
        
        # Press login button
        driver.find_element(By.ID, "login-button").click()
        
        # Verify user is incorrect
        title = driver.find_element(By.)
    
    driver.quit()
