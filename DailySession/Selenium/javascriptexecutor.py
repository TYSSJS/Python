
# # to open new tab
from selenium import webdriver
#
# # to interact with a window, we need to set the context to that
#
driver = webdriver.Chrome()
# first tab
# driver.get("https://www.redit.com")

#second tab
# driver.execute_script("window.open('about:blank','tab2');")

#go to seleniumhq.org-->download-->javadoc
# driver.get("https://www.seleniumhq.org/download/")
# javadoc = driver.find_element_by_link_text("Javadoc")
# javadoc.click()
# driver.implicitly_wait(20)
# frames = driver.find_element_by_xpath("(//ul[@class = 'navList']/li/a[. = 'Frames'])[1]")
# frames.click()

#scroll
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.execute_script("window.scrollTo(2,document.body.scrollHeight)")
print("scrolling")
# driver.close()

#
# driver.get("https://www.vtiger.com")
# privacy = driver.find_elements_by_xpath("//li/descendant::a[text()='Privacy Policy']")
# driver.execute_script("arguments[0].scrollIntoView();",privacy)