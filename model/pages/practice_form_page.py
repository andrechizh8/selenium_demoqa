import time

from model.pages.base_page import BasePage
from model.components.controls import DatePicker, RadioButton, CheckBox
from model.utils.path_to_file import file_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PracticeFormPage(BasePage):

    def type_first_name(self, value):
        self.element_is_visible(By.ID, "firstName").send_keys(value)
        return self

    def type_last_name(self, value):
        self.element_is_visible(By.ID, "lastName").send_keys(value)
        return self

    def type_email(self, value):
        self.element_is_visible(By.ID, "userEmail").send_keys(value)
        return self

    def type_phone(self, value):
        self.element_is_visible(By.ID, "userNumber").send_keys(value)

    def type_address(self, value):
        self.element_is_visible(By.ID, "currentAddress").send_keys(value)
        return self

    def select_gender(self, value):
        RadioButton(self.elements_is_visible(By.CSS_SELECTOR, "[for^=gender-radio]")).set_radio(value)
        return self

    def select_date(self, value):
        DatePicker(self.element_is_visible(By.ID, "dateOfBirthInput")).set_date(value)
        return self

    def select_hobby(self, value):
        CheckBox(self.elements_is_visible(By.CSS_SELECTOR, "[for^=hobbies-checkbox]")).set_hobby(value)
        return self

    def select_subject(self, value):
        self.element_is_visible(By.ID, "subjectsInput").send_keys(value)
        self.element_is_visible(By.ID, "subjectsInput").send_keys(Keys.TAB)
        return self

    def upload_file(self, value):
        file_path(self.element_is_visible(By.ID, "uploadPicture"), value)
        return self

    def set_state(self, value):
        self.element_is_visible(By.ID, "state").click()
        self.element_is_visible(By.CSS_SELECTOR, 'input[id="react-select-3-input"]').send_keys(value, Keys.ENTER)
        return self

    def set_city(self, value):
        self.element_is_visible(By.ID, "city").click()
        self.element_is_visible(By.CSS_SELECTOR, 'input[id="react-select-4-input"]').send_keys(value, Keys.ENTER)
        time.sleep(5)
        return self

    def select_submit(self):
        self.element_is_visible(By.ID, "submit").click()
        return self

    def check_info(self):
        self.elements_is_visible(By.ID, "example-modal-sizes-title-lg")


