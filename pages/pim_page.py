from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class PimPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    EMP_ID = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")

    def open_pim(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PIM_MENU)
        ).click()

    def take_screenshot(self, test_name, step_name):
        path = f"screenshots/{test_name}"
        os.makedirs(path, exist_ok=True)
        self.driver.get_screenshot_as_file(f"{path}/{step_name}.png")

    # 🔥 FIXED METHOD (NOW ACCEPTS test_name)
    def enter_emp_id(self, emp_id, test_name):

        field = self.wait.until(
            EC.visibility_of_element_located(self.EMP_ID)
        )

        field.clear()
        field.send_keys(emp_id)

        # wait until value is actually set
        self.wait.until(
            lambda d: field.get_attribute("value") == emp_id
        )

        # screenshot
        self.take_screenshot(test_name, "emp_id_entered")

        return field.get_attribute("value")