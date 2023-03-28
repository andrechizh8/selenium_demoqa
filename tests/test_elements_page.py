import time
import allure
from model.data.user_data import user
from model.pages.elements_page import RadioPage, TextBoxPage, ButtonPage


@allure.tag('UI', 'WEB')
@allure.description('Demoqa UI test')
@allure.label('owner', 'andrechizh8')
@allure.feature('UI')
@allure.story('Radio  Page')
class TestRadioButtonPage:
    def test_radio_form(self, driver):
        with allure.step("Open page"):
            form = RadioPage(driver, url="https://demoqa.com/radio-button")
            form.open()

        with allure.step("Select radio"):
            form.select_radio(user.like)

        with allure.step("Check selected"):
            form.check_selected(user.like)


@allure.tag('UI', 'WEB')
@allure.description('Demoqa UI test')
@allure.label('owner', 'andrechizh8')
@allure.feature('UI')
@allure.story('Text box Page')
class TestTextBox:
    def test_text_box(self, driver):
        with allure.step("Open page"):
            form = TextBoxPage(driver, url="https://demoqa.com/text-box")
            form.open()
        with allure.step("Fill name"):
            form.type_full_name(user.first_name)

        with allure.step("Fill email"):
            form.type_email(user.email)

        with allure.step("Fill address"):
            form.type_address(user.address)
            form.type_perm_address(user.address)

        with allure.step("click submit"):
            form.click_submit()


@allure.tag('UI', 'WEB')
@allure.description('Demoqa UI test')
@allure.label('owner', 'andrechizh8')
@allure.feature('UI')
@allure.story('Button page Page')
class TestButtonPage:

    def test_buttons(self, driver):
        with allure.step("Open page"):
            page = ButtonPage(driver, url="https://demoqa.com/buttons")
            page.open()

        with allure.step("Double click"):
            page.double_click_on_button()

        with allure.step("Right click"):
            page.right_click_on_button()

        with allure.step("Check double click"):
            page.check_correct_double_click()

        with allure.step("Check right click"):
            page.check_correct_right_click()
