from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://google.com')

search = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
search.send_keys("Hello World")
search.send_keys(Keys.RETURN)

secondLink = driver.find_element(By.XPATH, "//*[@id='rso']/div[4]/div/div/div/div/a")
secondLink.click()
