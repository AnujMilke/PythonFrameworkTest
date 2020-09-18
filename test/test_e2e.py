import time

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.xfail
class TestOne(BaseClass):
    def test_e2e(self):
        driver = self.driver
        homepage = HomePage(driver)
        checkoutpage = homepage.shopItems()
        time.sleep(4)
        checkoutpage.getCardTitle().click()
        time.sleep(2)
        confirmationPage = checkoutpage.getCheckOutLink()
        time.sleep(4)
        confirmationPage.getCheckOutLink2().click()
        confirmationPage.getTxtCountry().send_keys("ind")
        wait = WebDriverWait(driver, 10)

        mylist = driver.find_elements_by_xpath("//div[@class='suggestions']//ul//li")
        for l in mylist:
            if l.text == 'India':
                wait.until(expected_conditions.presence_of_element_located(l))
                l.click()

        driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        driver.find_element_by_xpath("//input[@value='Purchase']").click()

        driver.find_element_by_class_name("alert").is_displayed()
        time.sleep(4)
