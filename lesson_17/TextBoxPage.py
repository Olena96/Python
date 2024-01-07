from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        # self.full_name_field = (By.XPATH, "//input[@id='userName']")  # дублювання доступу до поля юзер нейм, але через xPAXTH
        self.full_email_field = (By.ID, "userEmail")
        self.full_current_text_area_field = (By.ID, "currentAddress")
        self.full_permanent_text_area_field = (By.CSS_SELECTOR, "textarea#permanentAddress")  # для різноманіття, можна було по айті як попереднє
        self.submit_btn = (By.ID, "submit")

    def open(self) -> "TextBoxPage":
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.driver.find_element(*self.full_name_field).clear()

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)

    #__________________________________________________________________________________________
    # todo реалізувати(метод clear and fill) для полів Email, Current Address, Permanent Address
    # Залити на окрему бранчу на гітхабі назва довільна(по можливості).

    #Email
    def clear_full_email_field(self) -> None:
        self.driver.find_element(*self.full_email_field).clear()

    def fill_full_email_field(self, text: str) -> None:
        self.driver.find_element(*self.full_email_field).send_keys(text)

    #Current Address
    def clear_full_current_text_area(self) -> None:
        self.driver.find_element(*self.full_current_text_area_field).clear()

    def fill_full_current_text_area(self, text: str) -> None:
        self.driver.find_element(*self.full_current_text_area_field).send_keys(text)

    #Permanent Address
    def clear_full_permanent_text_area(self) -> None:
        self.driver.find_element(*self.full_permanent_text_area_field).clear()

    def fill_full_permanent_text_area(self, text: str) -> None:
        self.driver.find_element(*self.full_permanent_text_area_field).send_keys(text)
    #________________________________________________________________________________________

    def click_submit(self) -> None:
        self.driver.find_element(*self.submit_btn).click()