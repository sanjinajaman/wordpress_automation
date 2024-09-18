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

    # Step 4: Wait for the WP Dark Mode settings page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Accessibility Settings")))

    # Step 5: Click on the "Accessibility Settings" tab
    driver.find_element(By.LINK_TEXT, "Accessibility Settings").click()

    # Step 6: Locate the "Keyboard Shortcut" setting and disable it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wp-dark-mode-disable-keyboard")))
    keyboard_shortcut_checkbox = driver.find_element(By.ID, "wp-dark-mode-disable-keyboard")

    # Disable the Keyboard Shortcut if it is enabled
    if keyboard_shortcut_checkbox.is_selected():
        keyboard_shortcut_checkbox.click()
        print("Keyboard Shortcut has been disabled.")
    else:
        print("Keyboard Shortcut is already disabled.")

    # Step 7: Save the changes
    save_button = driver.find_element(By.ID, "weblizar_page_anim_submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "weblizar_page_anim_submit")))
    save_button.click()

    print("Changes have been saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:

    driver.quit()
