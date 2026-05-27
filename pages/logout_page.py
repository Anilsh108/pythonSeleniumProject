# pages/logout_page.py

import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    USER_DROPDOWN = (
        By.XPATH,
        "//span[@class='oxd-userdropdown-tab']"
    )

    LOGOUT_OPTION = (
        By.XPATH,
        "//a[normalize-space()='Logout']"
    )

    LOGIN_HEADER = (
        By.XPATH,
        "//h5[normalize-space()='Login']"
    )

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_user_dropdown(self):
        self.wait.until(
            EC.element_to_be_clickable(self.USER_DROPDOWN)
        ).click()

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_OPTION)
        ).click()

    def wait_for_login_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.LOGIN_HEADER
            )
        )

    def take_screenshot(self, test_name, step_name):

        date_folder = datetime.now().strftime("%Y-%m-%d")

        screenshot_dir = os.path.join(
            "screenshots",
            date_folder,
            test_name
        )

        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(
            screenshot_dir,
            f"{step_name}.png"
        )

        self.driver.save_screenshot(screenshot_path)

    def logout(self, test_name):

        self.click_user_dropdown()

        self.click_logout()

        self.wait_for_login_page()

        self.take_screenshot(
            test_name,
            "after_logout_homepage"
        )