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

driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.get("http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2Flocalhost%2Fwordpress%2F")
driver.find_element(By.ID, "user_login").send_keys("adminwppool")
driver.find_element(By.ID, "user_pass").send_keys("admin123#FS")
driver.find_element(By.ID, "wp-submit").click()
driver.maximize_window()

try:
    # Wait for the dashboard page to load and dark mode toggle to be visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wpadminbar")))

    # Navigate to the WP Dark Mode settings (adjust the selector as per your configuration)
    driver.get("http://localhost/wordpress/wp-admin/admin.php?page=dracula")

    # Toggle Dark Mode if it is off
    toggle_button = driver.find_element(By.ID, "wpwrap")

    if "checked" not in toggle_button.get_attribute("class"):
        toggle_button.click()

    # Validate if dark mode is applied
    dark_mode_applied = driver.find_element(By.TAG_NAME, "body").get_attribute("class")

    if "dark-mode" in dark_mode_applied:
        print("Dark mode is working.")
    else:
        print("Dark mode is not applied.")

finally:
    # Close the browser
    driver.quit()