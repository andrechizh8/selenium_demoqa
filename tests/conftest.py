import pytest
from model.components import attach
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    yield driver

    attach.add_screenshots(driver)
    attach.add_html(driver)
    attach.add_logs(driver)

    driver.quit()
