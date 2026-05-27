import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class automationTestPractice:

    NAME_INPUT = (
        By.XPATH,
        "//label[text()='Name:']/following::input[1]"
    )

    GENDER_RADIO = (
        By.XPATH,
        "//input[@id='male']"
    )

    COLOR_OPTION = (
        By.XPATH,
        "//option[text()='Red']"
    )

    SINGLE_FILE_UPLOAD = (
        By.XPATH,
        "//input[@id='singleFileInput']"
    )

    MULTIPLE_FILE_UPLOAD = (
        By.XPATH,
        "//input[@id='multipleFilesInput']"
    )

    START_BUTTON = (
        By.XPATH,
        "//button[text()='START']"
    )

    DRAG_ELEMENT = (
        By.XPATH,
        "//p[text()='Drag me to my target']"
    )

    DROP_ELEMENT = (
        By.XPATH,
        "//div[@id='droppable']"
    )

    def __init__(self, driver, timeout=20):

        self.driver = driver

        self.wait = WebDriverWait(driver, timeout)

        self.action = ActionChains(driver)

    def take_screenshot(self, test_name, step_name):

        date_folder = datetime.now().strftime("%Y-%m-%d")

        screenshot_path = os.path.join(
            "screenshots",
            date_folder,
            test_name
        )

        os.makedirs(screenshot_path, exist_ok=True)

        file_name = os.path.join(
            screenshot_path,
            f"{step_name}.png"
        )

        self.driver.save_screenshot(file_name)

    def enter_username(self, username, test_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.NAME_INPUT
            )
        ).send_keys(username)

        self.take_screenshot(
            test_name,
            "entered_username"
        )

    def select_gender(self, test_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.GENDER_RADIO
            )
        ).click()

        self.take_screenshot(
            test_name,
            "selected_gender"
        )

    def select_color(self, test_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.COLOR_OPTION
            )
        ).click()

        self.take_screenshot(
            test_name,
            "selected_color"
        )

    def upload_single_file(self, file_path, test_name):

        self.wait.until(
            EC.presence_of_element_located(
                self.SINGLE_FILE_UPLOAD
            )
        ).send_keys(file_path)

        self.take_screenshot(
            test_name,
            "single_file_uploaded"
        )

    def upload_multiple_file(self, file_path, test_name):

        self.wait.until(
            EC.presence_of_element_located(
                self.MULTIPLE_FILE_UPLOAD
            )
        ).send_keys(file_path)

        self.take_screenshot(
            test_name,
            "multiple_file_uploaded"
        )

    def click_dynamic_button(self, test_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.START_BUTTON
            )
        ).click()

        self.take_screenshot(
            test_name,
            "dynamic_button_clicked"
        )

    def perform_drag_and_drop(self, test_name):

        source = self.wait.until(
            EC.visibility_of_element_located(
                self.DRAG_ELEMENT
            )
        )

        target = self.wait.until(
            EC.visibility_of_element_located(
                self.DROP_ELEMENT
            )
        )

        self.action.drag_and_drop(
            source,
            target
        ).perform()

        self.take_screenshot(
            test_name,
            "drag_and_drop_completed"
        )