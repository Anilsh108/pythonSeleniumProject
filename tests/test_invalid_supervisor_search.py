from pages.login_page import LoginPage
from pages.pim_page import PimPage
from config import URL, USERNAME, PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_pim_emp_id(setup, request):

    driver = setup
    driver.get(URL)

    test_name = request.node.name

    login = LoginPage(driver)
    pim = PimPage(driver)

    # ---------------- LOGIN ---------------- #
    login.login(USERNAME, PASSWORD, test_name)

    # wait dashboard
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[text()='Dashboard']")
        )
    )

    # ---------------- PIM ---------------- #
    pim.open_pim()

    # ---------------- EMP ID ---------------- #
    value = pim.enter_emp_id("12345", test_name)

    # ---------------- ASSERTION ---------------- #
    assert value.strip() == "12345", f"❌ Expected 12345 but got '{value}'"