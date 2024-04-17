from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = 'C:\\Users\\hp\\Downloads\\chromedriver-win6\\chromedriver-win64\\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
s = Service(executable_path=path) 
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://www.google.com/');
app=driver.find_element(By.XPATH,"(//a[contains(@aria-label, 'Google apps')])")
app.click()
driver.switch_to.frame("app")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//li/a//span[text()='YouTube']"))).click()
WebDriverWait(driver,10).until(EC.url_contains('https://www.youtub.com/'))
driver.quit()

#Custom xpaths- app - scans whole html page, finds a tags and then finds aria-label attribute(@) is Google apps
#contain function is used to locate aria-label
#youtube- finds all list tags then inside anchor/a tags then span then checks text is YouTube