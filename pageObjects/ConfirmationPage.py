from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    checkoutLink = (By.XPATH, "//button[contains(text(),'Checkout ')]")
    countryTxt = (By.CSS_SELECTOR, "#country")

    def getCheckOutLink2(self):
       return self.driver.find_element(*ConfirmationPage.checkoutLink)

    def getTxtCountry(self):
        return self.driver.find_element(*ConfirmationPage.countryTxt)