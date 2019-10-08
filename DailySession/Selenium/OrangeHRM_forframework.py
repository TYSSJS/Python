import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()
ele=first_menu=driver.find_elements_by_xpath("//a[@class='firstLevelMenu']")
l=[]
for i in ele:
    l.append(i.text)
print(l)

for i in range(len(l)):
    driver.find_element_by_xpath("//a[@class='firstLevelMenu']/b[text()='"+l[i]+"']").click()

time.sleep(1)
driver.find_element_by_id("welcome").click()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Logout']").click()
