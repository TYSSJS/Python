from selenium import webdriver
# 1.	Login to facebook and print number of friends online and offline and use assert wherever possible
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element_by_id("email").send_keys("manuamritalethe@yahoo.co.in")
driver.find_element_by_id("pass").send_keys("sarath@1985")
driver.find_element_by_id("u_0_b").click()
# a=driver.switch_to.alert
# a.accept()
online= driver.find_elements_by_xpath("//span[@aria-label='Active Now']")
for i in online:
    print(i.text)