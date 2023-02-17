import selenium
from selenium import webdriver
#from selenium.webdriver.common.Keys import Keys

user = "17013"
pwd = "Sandesh@123"

driver = webdriver.Edge(r"msedgedriver.exe")
driver.implicitly_wait(8000)

driver.get("https://sharekonnect.sharekhan.com/default.aspx?")

driver.implicitly_wait(8000)

element = driver.find_element("id","UserName")
element.send_keys(user)

element = driver.find_element("id","PasswordText")
element.send_keys(pwd)

driver.implicitly_wait(8000)

# element = driver.find_element("id","btnLogin")
element = driver.find_element(by.ID,"btnLogin")
element.click()

# element.send_keys(Keys.RETURN)
