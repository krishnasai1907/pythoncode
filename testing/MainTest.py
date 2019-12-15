from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

from testing.pomfile import  pomfile


class MainTest:
    driver=webdriver.Chrome(executable_path="C:\\Users\\Krishna\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.goindigo.in/")
    driver.set_page_load_timeout(100)
    driver.implicitly_wait(10)
    roundTrip="//label[contains(text(),'Round Trip')]"
    source="or-src"
    driver.find_element(By.XPATH,roundTrip).click()
    time.sleep(2)
    driver.find_element(By.NAME,source).click()
    driver.find_element(By.NAME, source).send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME,source).send_keys("CJB")
    time.sleep(2)
    driver.find_element_by_name(source).send_keys(Keys.ENTER)
    driver.find_element_by_name("or-dest").clear()
    time.sleep(1)
    driver.find_element_by_name("or-dest").send_keys("MAA")
    time.sleep(2)
    driver.find_element_by_name("or-dest").send_keys(Keys.ENTER)
    # time.sleep(2)
    driver.execute_script("window.scrollTo(0,140)")
    wait = WebDriverWait(driver, 45)
    time.sleep(2)
    driver.find_element_by_name("or-depart").click()
    driver.find_element_by_xpath("(//td[@class=' ui-datepicker-week-end ']/child::a)[1]").click()
    time.sleep(2)
    driver.find_element_by_name("or-return").click()
    driver.find_element_by_xpath("(//td[@class=' ui-datepicker-week-end ']/child::a)[2]").click()
    driver.find_element_by_name("passenger").click()
    driver.execute_script("window.scrollTo(0,140)")
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='passenger-dropdown pax-selection-row']//label[contains(text(),'Adult(s)')]/following-sibling::div/descendant::span[@class='icon-plus']")))
    driver.find_element_by_xpath("//div[@class='passenger-dropdown pax-selection-row']//label[contains(text(),'Adult(s)')]/following-sibling::div/descendant::span[@class='icon-plus']").click()
    driver.find_element_by_xpath("//div[@class='passenger-done-blck']//button").click()
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[contains(text(),'Search Flight')]")))
    driver.find_element_by_xpath("//span[contains(text(),'Search Flight')]").click()
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='trips-body ios-scroll rw']/descendant::span[@class='flightNo']")))
    driver.get_screenshot_as_file(".\\testing\\file.png")
    driver.save_screenshot(".\\testing\\screge.png")
    print(driver.find_element_by_xpath("//div[@class='trips-body ios-scroll rw']/descendant::span[@class='flightNo']").text)
    driver.minimize_window()
    driver.close()

