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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Customization")))

    # Step 5: Click on the "Customization" tab
    driver.find_element(By.LINK_TEXT, "Customization").click()

    # Step 6: Wait for the "Switch Settings" option and click it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Switch Settings")))
    driver.find_element(By.LINK_TEXT, "Switch Settings").click()

    # Step 7: In "Switch Customization", select Custom Switch size
    # Locate the dropdown for switch size and select a custom option
    select = Select(driver.find_element(By.ID, "custom_switch_size_dropdown"))
    select.select_by_visible_text("Custom")  # Selecting the Custom option

    # Step 8: Scale the custom switch size to 220
    scale_input = driver.find_element(By.ID,"switch_scale_slider")
    scale_input.clear()  # Clear existing value
    scale_input.send_keys("220")  # Set the value to 220

    # Step 9: Save the changes
    save_button = driver.find_element(By.ID, "weblizar_page_anim_submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "weblizar_page_anim_submit")))
    save_button.click()

    print("Switch size set to Custom and scaled to 220 successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
