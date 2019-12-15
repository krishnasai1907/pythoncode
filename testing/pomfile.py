from selenium.webdriver.common.by import By


class pomfile:
    def __int__(self,driver):
        self.driver=driver

        self.username="//label[contains(text(),'Round Trip')]"
    def getRoundTrip(self):
        self.driver.find_elements_by_xpath(self.username).click()

