from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # ---------------- LOCATORS ---------------- #

    username = (By.NAME, "username")

    password = (By.NAME, "password")

    login_btn = (By.XPATH, "//button[@type='submit']")

    dashboard_text = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    # ---------------- SCREENSHOT METHOD ---------------- #

    def take_screenshot(self, test_name, step_name):

        date_folder = datetime.now().strftime("%Y-%m-%d")

        path = f"screenshots/{date_folder}/{test_name}"

        os.makedirs(path, exist_ok=True)

        file_path = f"{path}/{step_name}.png"

        self.driver.get_screenshot_as_file(file_path)

    # ---------------- LOGIN METHOD ---------------- #

    def login(self, user, pwd, test_name):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(user)

        self.driver.find_element(*self.password).send_keys(pwd)

        # Screenshot before login
        self.take_screenshot(
            test_name,
            "after_entering_credentials"
        )

        self.driver.find_element(*self.login_btn).click()

        # Wait for dashboard page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.dashboard_text)
        )

        time.sleep(2)

        # Screenshot after login
        self.take_screenshot(
            test_name,
            "after_login_homepage"
        )