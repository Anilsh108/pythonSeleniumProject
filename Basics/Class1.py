from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

# Launch browser
# webdriver-helps to selenium to communicate with browsergit 
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# Open OrangeHRM
driver.get("https://testautomationpractice.blogspot.com/")

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# dropdown=driver.find_element(By.ID,"country")
# select=Select(dropdown)
dropdown1=driver.find_element(By.ID,"colors")
select=Select(dropdown1)
select.select_by_visible_text("Blue")
select.select_by_visible_text("Yellow")
time.sleep(3)
# select.deselect_by_visible_text("Blue")
# select.deselect_by_value("blue")
# select.deselect_by_index(1)
# select.deselect_by_value("blue")
select.deselect_all()
time.sleep(3)

# select.select_by_visible_text("Canada")
# select.select_by_index(3)
# select.select_by_value("india")
# selected=select.first_selected_option.text
# print(selected)
# options=select.options
# for option in options:
#     print(options)

time.sleep(10)

# element=driver.find_element(By.XPATH,"//h2[text()='Drag and Drop']")
# element=driver.find_element(By.XPATH,"//a[text()='GUI Elements']")
# actions=ActionChains(driver)
# actions.move_to_element(element).perform()
# actions.context_click(element).perform()
# actions.double_click(element).perform()

# source=driver.find_element(By.XPATH,"//p[text()='Drag me to my target']")
# target=driver.find_element(By.XPATH,"//p[text()='Drop here']")
# actions.drag_and_drop(source,target).perform()

# slider=driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
# actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
# time.sleep(10)
# actions.click_and_hold(slider).pause(3).release().perform()
# actions.click_and_hold(slider).pause(3).release().perform()
# actions.click_and_hold(slider).move_by_offset(32,0).release().perform()
# time.sleep(10)
# driver.minimize_window()
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.close()

# element=driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# print(len(element))

# wait=WebDriverWait(driver,10)
# name=wait.until(
# EC.visibility_of_element_located((By.XPATH,"//input[@id='name']"))
# )
# name.send_keys("admin123")

# elements=driver.find_elements(By.XPATH,'//label[@class="form-check-label"]')
# for content in elements:
#     print(content.text)
# element.send_keys("admin123")

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