import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.implicitly_wait(10)

click_contribute=driver.find_element_by_xpath("//a[text()='Contribute']")
act=ActionChains(driver)
act.move_to_element(click_contribute).perform()
driver.find_element_by_xpath("//a[text()='Droppable']").click()
# time.sleep(5)
act1=ActionChains(driver)
# fr=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to.frame(0)
src=driver.find_element_by_xpath("//p[text()='Drag me to my target']")
dest=driver.find_element_by_xpath("//p[text()='Drop here']")

# drag and drop
# act1.drag_and_drop(src,dest).perform()
act1.click_and_hold(src).move_to_element(dest).perform()
driver.close()