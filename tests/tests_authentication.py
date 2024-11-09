from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# tests_authentication.py
# These tests are designed to test the authentication function of the https://www.saucedemo.com application

# Test to make sure page loads
def test_page_load():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"
    driver.quit()
    
# Test User logins and logout
# users: standard_user, problem_user, performance_glitch_user, error_user, visual_user
# passwords: secret_sauce
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
    
# Test fail login with correct usernames and incorrect password
def test_fail_login_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    users = ["standard_user", "locked_out_user","problem_user", "performance_glitch_user", "error_user", "visual_user"]
    
    for user in users:
        # Enter in username and password
        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.ID, "password").send_keys("test123")
        
        # Press login button
        driver.find_element(By.ID, "login-button").click()
        
        # Verify user is incorrect
        error = driver.find_element("xpath", '//*[@data-test="error"]')
        assert(error)

    driver.quit()

# Test fail login with incorrect username and incorrect password
def test_fail_login_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Enter in username and password
    driver.find_element(By.ID, "user-name").send_keys("test123")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Press login button
    driver.find_element(By.ID, "login-button").click()
    
    # Verify user is incorrect
    error = driver.find_element("xpath", '//*[@data-test="error"]')
    assert(error)
    driver.quit()