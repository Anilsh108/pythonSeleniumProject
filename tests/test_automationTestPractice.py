from pages.automationTestPractice import automationTestPractice
from config import AUTOMATION_PRACTICE_URL


def test1(setup, request):

    driver = setup

    driver.get(AUTOMATION_PRACTICE_URL)

    test_name = request.node.name

    test = automationTestPractice(driver)

    test.enter_username(
        "suchitra",
        test_name
    )

    test.select_gender(
        test_name
    )

    # test.select_color(
    #     test_name
    # )

    test.upload_single_file(
        r"C:\Users\Anil Kanaji\Downloads\test (1).txt",
        test_name
    )

    test.upload_multiple_file(
        r"C:\Users\Anil Kanaji\Downloads\test (1).txt",
        test_name
    )

    test.click_dynamic_button(
        test_name
    )

    test.perform_drag_and_drop(
        test_name
    )