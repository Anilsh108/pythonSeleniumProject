from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
# webdriver-helps to selenium to communicate with browser
driver = webdriver.Chrome()

# Open OrangeHRM
driver.get("https://testautomationpractice.blogspot.com/")

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.close()

# time.sleep(10)
# element=driver.find_element(By.ID, "name")
# element.send_keys("admin123")
# time.sleep(10)
# data=element.get_attribute("value")
# print(data)
# time.sleep(5)
# driver.find_element(By.ID, "name").clear()
# time.sleep(10)
# driver.find_element(By.XPATH,"//button[@type='submit']").submit()

# element=driver.find_element(By.XPATH,"//button[@type='submit']")
# result1=element.is_displayed()
# print(result1)
# result2=element.is_enabled()
# print(result2)
# print(element.text)
# result3=element.get_attribute("type")
# print(result3)


# result3=element.get_attribute("type")
# print(result3)
# print(element.text)
# time.sleep(5)






# Enter username
# wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))).send_keys("Dhanalaxmi")

# wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Udemy Courses"))).click()



# # Enter password
# # Click login
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# # ✅ Validate login (Dashboard visible)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

# # ✅ Print success message
# print("✅ Logged in successfully")

# # Close browser
# driver.quit()