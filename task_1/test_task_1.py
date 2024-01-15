#* Сделать выборку контактов из списка
#* Экспортировать выбранные контакты в .CSV файл
#* Убедиться, что в файле содержатся нужные записи
import pandas as pd
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCSV:

    LABEL_LOCATOR = ("xpath", "//li[contains(@class, 'MuiListItem-dense')]//span[text()='musician']")
    EXPORT_LOCATOR = ("xpath", "//button[@aria-label='Export']")

    first_name = "Natalie"
    last_name = "Kutfdadsfadsfch"
    email = "Natalie60@gmail.com"

    path = f"{os.getcwd()}/downloads/contacts.csv"

    def setup(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        preferences = {
            "download.default_directory": f"{os.getcwd()}/downloads"
        }
        options.add_experimental_option("prefs", preferences)
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.driver.get("https://release-crm.qa-playground.com/#/contacts")

    def test_contact_in_csv(self):
        self.wait.until(EC.visibility_of_element_located(self.LABEL_LOCATOR)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.EXPORT_LOCATOR)).click()
        time.sleep(2)
        contacts = pd.read_csv(self.path)
        result = contacts[
            (contacts["first_name"] == self.first_name) & \
            (contacts["last_name"] == self.last_name) & \
            (contacts["email"] == self.email)
            ].any().any()
        assert result == True, "Такой записи нет"



