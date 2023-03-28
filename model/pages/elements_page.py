from model.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from model.components.controls import RadioButton


class ButtonPage(BasePage):

    def double_click_on_button(self):
        self.action_double_click(self.element_is_clickable(By.ID, "doubleClickBtn"))
        return self

    def right_click_on_button(self):
        self.action_right_click(self.element_is_clickable(By.ID, "rightClickBtn"))
        return self

    def check_correct_double_click(self):
        element = self.element_is_visible(By.ID, "doubleClickMessage")
        assert element.text == "You have done a double click"
        return self

    def check_correct_right_click(self):
        element = self.element_is_visible(By.ID, "rightClickMessage")
        assert element.text == "You have done a right click"
        return self


class RadioPage(BasePage):

    def select_radio(self, value):
        RadioButton(self.elements_is_visible(By.CSS_SELECTOR, '[class^="custom-control"]')).set_radio(value)
        return self

    def check_selected(self, value):
        element = self.element_is_visible(By.CSS_SELECTOR, "[class='text-success']")
        assert element.text == value
        return self


class TextBoxPage(BasePage):

    def type_full_name(self, value):
        self.element_is_visible(By.ID, "userName").send_keys(value)
        return self

    def type_email(self, value):
        self.element_is_visible(By.ID, "userEmail").send_keys(value)
        return self

    def type_address(self, value):
        self.element_is_visible(By.ID, "currentAddress").send_keys(value)
        return self

    def type_perm_address(self, value):
        self.element_is_visible(By.ID, "permanentAddress").send_keys(value)
        return self

    def click_submit(self):
        self.element_is_clickable(By.ID, "submit").click()
        return self
