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
    # Step 1: Navigate to the front end of the website
    driver.get("http://localhost/wordpress/wp-login.php?redirect_to=http%3A%2F%2Flocalhost%2Fwordpress%2F")

    # Step 2: Wait for the page to load and locate the Dark Mode switch
    # Adjust the ID or class of the dark mode switch based on your specific site setup
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "wp-dark-mode-switch")))

    # Step 3: Get initial background color (to compare later)
    body_element = driver.find_element(By.TAG_NAME, "body")
    initial_bg_color = body_element.value_of_css_property("background-color")
    print(f"Initial background color: {initial_bg_color}")

    # Step 4: Toggle Dark Mode by clicking the switch
    dark_mode_switch = driver.find_element(By.CLASS_NAME, "wp-dark-mode-switch")  # Adjust based on your site
    dark_mode_switch.click()

    # Step 5: Wait for the background color or class change
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.TAG_NAME, "body").value_of_css_property("background-color") != initial_bg_color
    )

    # Step 6: Get the background color after toggling dark mode
    final_bg_color = body_element.value_of_css_property("background-color")
    print(f"Background color after enabling Dark Mode: {final_bg_color}")

    # Step 7: Validate if Dark Mode is applied (checking if the color changed)
    if initial_bg_color != final_bg_color:
        print("Dark Mode is working correctly.")
    else:
        print("Dark Mode is not working as expected.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after completion
    driver.quit()
