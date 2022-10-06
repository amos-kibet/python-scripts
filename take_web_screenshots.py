# Take Web Screenshots
# pip install selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.medium.com')
H = driver.execute_script("return document.body.scrollHeight")
W = driver.execute_script("return document.body.scrollWidth")
driver.set_window_size(W, H)
driver.find_element_by_tag_name('body')
driver.screenshot('screenshot.png')
