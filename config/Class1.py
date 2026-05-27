from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
time.sleep(2)

# Enter Username
driver.find_element(By.NAME, "username").send_keys("Admin")

# Enter Password
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click Login
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)

# Validation
if "dashboard" in driver.current_url.lower():
    print("✅ Login Successful")
else:
    print("❌ Login Failed")

# Close browser
driver.quit()