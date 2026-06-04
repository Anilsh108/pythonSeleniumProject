from config.config import URL, USERNAME, PASSWORD

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout(setup, request):

    driver = setup

    driver.get(URL)

    test_name = request.node.name

    login_page = LoginPage(driver)
    login_page.login(
        USERNAME,
        PASSWORD,
        test_name
    )

    logout_page = LogoutPage(driver)
    logout_page.logout(test_name)