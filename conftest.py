import pytest
from utils.driver_factory import get_driver
import os
import shutil

@pytest.fixture(scope="function")
def setup():

    # 🧹 Remove old screenshots before test starts
    if os.path.exists("screenshots"):
        shutil.rmtree("screenshots")

    os.makedirs("screenshots", exist_ok=True)

    driver = get_driver()
    yield driver
    driver.quit()