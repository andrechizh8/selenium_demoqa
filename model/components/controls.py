import time

from selenium.webdriver.common.keys import Keys


class RadioButton:
    def __init__(self, element):
        self.element = element

    def set_radio(self, value):
        for item in self.element:
            if item.text == value:
                item.click()


class DatePicker:
    def __init__(self, element):
        self.element = element

    def set_date(self, value):
        self.element.send_keys(Keys.CONTROL, "a")
        self.element.send_keys(value, Keys.ENTER)


class CheckBox:
    def __init__(self, element):
        self.element = element

    def set_hobby(self, value):
        for item in self.element:
            if item.text == value:
                item.click()
