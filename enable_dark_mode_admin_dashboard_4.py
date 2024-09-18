import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




driver =webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.maximize_window()

try:
    # Step 1: Log in to the WordPress admin dashboard
    driver.get("http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2Flocalhost%2Fwordpress%2F")
    driver.find_element(By.ID, "user_login").send_keys("adminwppool")
    driver.find_element(By.ID, "user_pass").send_keys("admin123#FS")
    driver.find_element(By.ID, "wp-submit").click()

    # Step 2: Wait for the admin dashboard to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wpadminbar")))

    # Step 3: Navigate to the WP Dark Mode settings page
    driver.get("http://localhost/wordpress/wp-admin/admin.php?page=dracula")


    # Step 4: Locate the "Admin Panel Dark Mode" checkbox
    admin_dark_mode_checkbox = driver.find_element(By.CLASS_NAME, "components-form-toggle__input")

    # Step 8: Check if Admin Dark Mode is enabled, if not, enable it
    if not admin_dark_mode_checkbox.is_selected():
        admin_dark_mode_checkbox.click()
        print("Admin Dashboard Dark Mode has been enabled.")
    else:
        print("Admin Dashboard Dark Mode is already enabled.")

    # Step 9: Save the changes
    save_button = driver.find_element(By.XPATH, '//*[@id="dracula-settings-app"]/div/div[2]/div[1]/div[2]/button/span')
    save_button.click()


    print("Changes have been saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    
    driver.quit()