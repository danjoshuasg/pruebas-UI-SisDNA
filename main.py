from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from B import script2
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
script2.Proof(driver,wait)