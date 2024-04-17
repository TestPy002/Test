from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

path = 'C:\\Users\\hp\\Downloads\\chromedriver-win6\\chromedriver-win64\\chromedriver.exe'  # Windows example

# Optional: Specify options for Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Uncomment to run in headless mode (without opening a visible browser window)
s = Service(executable_path=path) 
# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(service=s, options=chrome_options)

try:
    # Navigate to the GitHub login page
    driver.get('https://en.wikipedia.org/wiki/Resistor')
    c=driver.find_element(By.CLASS_NAME,"mw-logo-container")
    c.click()
    time.sleep(5)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL, 'a') #pressing Ctrl+A
# Open a new tab (Ctrl + T)
    #driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't')
    driver.execute_script("window.open('about:blank', '_blank');") #creates  new window
# Switch to the new tab
    driver.switch_to.window(driver.window_handles[1]) 
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    input = WebDriverWait(driver,10).until( EC.visibility_of_element_located((By.ID,"identifierId")) )
    input.send_keys('surveyandfeedback1to10@gmail.com')
    but=driver.find_element(By.XPATH,"//button//span[text()='Next']") #custom xpath for next button
    #but=driver.find_element(By.CSS_SELECTOR,'#identifierNext > div > button > span') #can use css selector also
    but.click()
    time.sleep(40)
finally:
    driver.quit()

#Xpath for next button - // - scans whole html, button tag, span tag, [text()='Next'] - checks text inside span in button tag is Next.