from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, 'name')
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    exampleCheck1 = (By.ID, "exampleCheck1")
    select = (By.ID, "exampleFormControlSelect1")
    inlineRadio1 = (By.ID, "inlineRadio1")
    bday = (By.NAME, "bday")
    sbmt = (By.XPATH, "//input[@type='submit']")

    def get_shop(self):
        return self.driver.find_element(*HomePage.shop)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_pwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def get_example_check1(self):
        return self.driver.find_element(*HomePage.exampleCheck1)

    def get_select(self):
        return self.driver.find_element(*HomePage.select)

    def get_inline_radio1(self):
        return self.driver.find_element(*HomePage.inlineRadio1)

    def get_inline_bday(self):
        return self.driver.find_element(*HomePage.bday)

    def get_inline_submit(self):
        return self.driver.find_element(*HomePage.sbmt)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage


