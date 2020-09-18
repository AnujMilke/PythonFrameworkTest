from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//a[contains(text(),'Blackberry')]/parent::h4/parent::div/following-sibling::div/button")
    checkOutLink = (By.PARTIAL_LINK_TEXT,"Checkout")

    def getCardTitle(self):
        return self.driver.find_element(*CheckOutPage.cardTitle)

    def getCheckOutLink(self):
        self.driver.find_element(*CheckOutPage.checkOutLink).click()
        confirmationpage = ConfirmationPage(self.driver)
        return confirmationpage