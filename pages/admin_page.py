from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime


class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ================= LOCATORS =================
    admin_menu = (By.XPATH, "//span[text()='Admin']")
    username_input = (By.XPATH, "//label[text()='Username']/following::input[1]")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
    status_dropdown = (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
    search_btn = (By.XPATH, "//button[normalize-space()='Search']")
    table_rows = (By.XPATH, "//div[@role='rowgroup']//div[@role='row']")

    # ================= REUSABLE DROPDOWN =================
    def select_dropdown(self, dropdown, value):
        self.wait.until(EC.element_to_be_clickable(dropdown)).click()

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@role='listbox']")
        ))

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[text()='{value}']")
        )).click()

    # ================= MAIN FUNCTION =================
    def search_user(self, username, test_name):

        # Click Admin Menu
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

        # Wait for Admin page
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h6[text()='Admin']")
        ))

        # Enter Username
        self.wait.until(EC.visibility_of_element_located(self.username_input)).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

        # Select filters
        self.select_dropdown(self.user_role_dropdown, "Admin")
        self.select_dropdown(self.status_dropdown, "Enabled")

        # Click Search
        self.wait.until(EC.element_to_be_clickable(self.search_btn)).click()

        # Wait for table
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))

        # Scroll to first row
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rows[0])

        # ================= SCREENSHOT =================
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

        # ================= VALIDATION =================
        found = False
        for row in rows:
            if username in row.text:
                found = True
                break

        assert found, f"{username} not found in search results"