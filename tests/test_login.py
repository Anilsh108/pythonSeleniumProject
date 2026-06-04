from pages.login_page import LoginPage
from config import URL, USERNAME, PASSWORD

def test_login(setup, request):
    driver = setup
    driver.get(URL)

    test_name = request.node.name

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD, test_name)

    assert "OrangeHRM" in driver.title