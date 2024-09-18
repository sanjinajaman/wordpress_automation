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

    # Step 3: Navigate to the page annimation settings page
    driver.get("http://localhost/wordpress/wp-admin/admin.php?page=weblizar-page-animation")

    driver.find_element(By.XPATH, '//*[@id="weblizar_page_in_trans"]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[2]/select/option[3]').click()


    save_button = driver.find_element(By.XPATH, '//*[@id="weblizar_page_anim_submit"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)

    # Wait for the Save Changes button to be clickable and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "weblizar_page_anim_submit")))


    print("Successfully enable Page-Transition Animation & change the Animation Effect")
    # driver.execute_script("arguments[0].click();", save_button)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after completion
    driver.quit()
    print("success")