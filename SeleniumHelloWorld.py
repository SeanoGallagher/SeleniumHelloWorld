from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True;

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://google.com')

search = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
search.send_keys("TonDone")
search.send_keys(Keys.RETURN)

secondLink = driver.find_element(By.XPATH, "//*[@id='rso']/div//a[1]")
secondLink.click()

text = driver.find_element(By.XPATH, "//*[@class='content-pair-text']/h1")
if(text.text.find("The easy way to manage hard work")):
    print("Text successfully found")
else:
    print("Text not found")
