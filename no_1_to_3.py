import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException





# Function to log in to WordPress
def login_to_wordpress(driver, username, password):
    driver.get("http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2Flocalhost%2Fwordpress%2F") # Change to your WordPress login URL
    #time.sleep(2)  # Wait for the page to load

    driver.find_element(By.ID, "user_login").send_keys(username)
    driver.find_element(By.ID, "user_pass").send_keys(password)
    driver.find_element(By.ID, "wp-submit").click()

    # Validate login by checking if the WordPress admin bar is visible
    time.sleep(3)  # Wait for the dashboard to load
    print("Login successful!")


# Function to check if WP Dark Mode plugin is active
def is_wp_dark_mode_active(driver):
    # Navigate to Plugins page
    driver.get("http://localhost/wordpress/wp-admin/plugins.php")
    time.sleep(2)  # Wait for the page to load

    # Search for "WP Dark Mode" in the plugins list
    try:
        wp_dark_mode_plugin = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form[2]/table/tbody/tr[2]/td[1]/strong")
        # Check if the plugin is active by looking for the 'Deactivate' button
        if "Deactivate" in wp_dark_mode_plugin.text:
            print("WP Dark Mode plugin is active.")
            return True
        else:
            print("WP Dark Mode plugin is installed but not active.")
            return True
    except Exception as e:
        print("WP Dark Mode plugin is not installed.")
        return False


# Function to install and activate the WP Dark Mode plugin
def install_and_activate_wp_dark_mode(driver):
    print("Installing WP Dark Mode plugin...")

    # Step 1: Go to "Add New Plugin" page
    driver.get("http://localhost/wordpress/wp-admin/plugin-install.php")
    time.sleep(2)

    # Step 2: Search for "WP Dark Mode"
    driver.find_element(By.ID, "search-plugins").send_keys("Dracula Dark Moder")


    # Step 3: Click "Install Now"
    active = driver.find_element(By.ID, "button button-disabled")
    active.click()

    # Step 4: Activate the plugin
    driver.find_element(By.CLASS_NAME, "button button-disabled").click()
    time.sleep(2)
    print("WP Dark Mode plugin installed and activated successfully!")


# Function to navigate to the WP Dark Mode settings page
def navigate_to_wp_dark_mode_settings(driver):
    print("Navigating to WP Dark Mode settings...")

    driver.find_element(By.CLASS_NAME,"dracula-toggle-icon").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul[2]/li[2]/div/div/div[1]/div[2]/span[2]").click()
    print("WP Dark Mode settings page loaded successfully!")


if __name__ == "__main__":
    driver = webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))  # Ensure to have ChromeDriver installed
    driver.maximize_window()


    wordpress_username = "adminwppool"
    wordpress_password = "admin123#FS"

    try:
        # Step 1: Log in to WordPress
        login_to_wordpress(driver, wordpress_username, wordpress_password)

        # Step 2: Check if "WP Dark Mode" plugin is active
        if is_wp_dark_mode_active(driver):
            # If active, navigate to WP Dark Mode settings
            navigate_to_wp_dark_mode_settings(driver)
        else:
            # If inactive or not installed, install and activate the plugin
            install_and_activate_wp_dark_mode(driver)

            # Navigate to WP Dark Mode settings after activation
            navigate_to_wp_dark_mode_settings(driver)

    finally:
        driver.quit()
