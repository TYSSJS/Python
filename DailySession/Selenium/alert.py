
#alert pop up
# below actions are performed in TC1_basicAlert.html
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Amritha/PycharmProjects/PythonProject/pySelenium/TC1_basicAlert.html")
# switch to alert me
# al_me=driver.find_element_by_id("show-alert")
# al_me.click()
# a=driver.switch_to.alert
# a.accept()
# time.sleep(10)
#switch to prompt me
# prompt_me = driver.find_element_by_id("show-prompt")
# prompt_me.click()
# a1=driver.switch_to.alert
# time.sleep(20)
# a1.send_keys("amrita")
# a1.accept()
#click on 'Confirm me'
confirm_me = driver.find_element_by_id("show-confirm")
confirm_me.click()
a = driver.switch_to.alert
a.accept()