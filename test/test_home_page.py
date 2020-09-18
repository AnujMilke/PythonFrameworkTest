import time

import pytest
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testdata.test_home_page_data import TestHomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_home_page(self, get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys("email@gmail.com")
        log.info(get_data["lastname"])
        homepage.get_pwd().send_keys(get_data["lastname"])
        homepage.get_example_check1().click()
        log.info(get_data["gender"])
        self.select_option_by_text(homepage.get_select(), get_data["gender"])
        homepage.get_inline_submit().click()

        time.sleep(10)
        self.driver.refresh()

    @pytest.fixture(params=TestHomePageData.getTestData("Testcase2"))
    def get_data(self, request):
        return request.param
