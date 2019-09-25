# import Actions as Actions
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(10)
driver.maximize_window()

move_to_element=driver.find_element_by_xpath("//a[text()='Best Sellers']")
act=ActionChains(driver)
act.move_to_element(move_to_element).perform()
