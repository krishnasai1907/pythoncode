from selenium import webdriver


class Setup:
    def __int__(self,driver):
        driver.maximize_window()
        driver.get("https://www.goindigo.in/")
        driver.set_page_load_timeout(100)
        driver.implicitly_wait(10)
