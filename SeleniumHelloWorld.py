from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://google.com')

search = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
search.send_keys("TonDone")
search.send_keys(Keys.RETURN)

secondLink = driver.find_element(By.XPATH, "//*[@id='rso']/div//a[1]")
secondLink.click()

text = driver.find_element(By.CLASS_NAME, "content-pair-text")
if(text.text.find("The easy way to manage hard work")):
    print("Text successfully found")
else:
    print("Text not found")
