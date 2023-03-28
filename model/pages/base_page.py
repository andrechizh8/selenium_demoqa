from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ES


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, by, selector):
        return wait(self.driver, timeout=3).until(ES.visibility_of_element_located((by, selector)))

    def element_is_clickable(self, by, selector):
        return wait(self.driver, timeout=3).until(ES.element_to_be_clickable((by, selector)))

    def element_is_selected(self, by, selector):
        return wait(self.driver, timeout=3).until(ES.element_to_be_selected((by, selector)))

    def go_to_element(self, by, selector):
        self.driver.execute_script("arguments[0].scrollIntoView();", (by, selector))

    def elements_is_visible(self, by, selector):
        return wait(self.driver, timeout=3).until(ES.visibility_of_any_elements_located((by, selector)))

    def action_double_click(self, selector):
        action = ActionChains(self.driver)
        action.double_click(selector)
        action.perform()

    def action_right_click(self, selector):
        action = ActionChains(self.driver)
        action.context_click(selector)
        action.perform()
