import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/GIT/devopsCourse/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://192.168.99.100:5000/")

text = driver.find_element_by_xpath("//*")
x = text.text.replace('World', '')
print(x)
