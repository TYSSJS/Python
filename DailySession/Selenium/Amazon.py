import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='text']").send_keys("mobiles",Keys.ENTER)
driver.find_element_by_xpath("(//i[@class='a-icon a-icon-checkbox'])[1]").click()
time.sleep(10)
primeEligible=driver.find_element_by_xpath("//span[text()='Prime Eligible']")
print("PrimeEligible ",primeEligible.is_enabled())
Elements=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for i in Elements:
    print(i.text)




