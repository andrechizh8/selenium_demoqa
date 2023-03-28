import allure
from model.pages.practice_form_page import PracticeFormPage
from model.data.user_data import user


@allure.tag('UI', 'WEB')
@allure.description('Demoqa UI test')
@allure.label('owner', 'andrechizh8')
@allure.feature('UI')
@allure.story('Form Page')
class TestForm:
    def test_practice_form(self, driver):
        with allure.step("Open page"):
            form = PracticeFormPage(driver, url="https://demoqa.com/automation-practice-form")
            form.open()

        with allure.step("Fill name"):
            form.type_first_name(user.first_name)
            form.type_last_name(user.last_name)

        with allure.step("Fill email"):
            form.type_email(user.email)

        with allure.step("Fill phone"):
            form.type_phone(user.phone)

        with allure.step("Fill address"):
            form.type_address(user.address)

        with allure.step("Select gender"):
            form.select_gender(user.gender)

        with allure.step("Select date"):
            form.select_date(user.date)

        with allure.step("Select subject"):
            form.select_subject(user.subjects)

        with allure.step("Select hobby"):
            form.select_hobby(user.hobby)

        with allure.step("Upload file"):
            form.upload_file(user.picture)

        with allure.step("Select state"):
            form.set_state(user.state)

        with allure.step("Select city"):
            form.set_city(user.city)
