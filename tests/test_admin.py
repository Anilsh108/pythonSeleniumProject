from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from config import URL, USERNAME, PASSWORD


def test_admin_user_search(setup, request):
    driver = setup
    driver.get(URL)

    test_name = request.node.name

    # Login
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD, test_name)

    # Admin Search
    admin = AdminPage(driver)
    admin.search_user("Admin", test_name)