from selenium import webdriver
import time

chrome_browser = webdriver.Chrome()
chrome_browser.get("https://demo.seleniumeasy.com/")

chrome_browser.maximize_window()
time.sleep(10)

# chrome_browser.quit()