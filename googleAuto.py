from selenium import webdriver
import time
# Specify the full path to your msedgedriver executable
msedgedriver_path = 'C:\\Users\\hp\\Downloads\\edgedriver_win64\\msedgedriver.exe'

# Create a new instance of the Microsoft Edge WebDriver with options
service = webdriver.EdgeService(executable_path=msedgedriver_path, service_log_path='NUL')
driver = webdriver.Edge(service=service)

# Example: Open Google and search for "Python programming"
driver.get('https://www.google.com/')
search_box = driver.find_element('name', 'q')
search_box.send_keys('Python programming')
search_box.submit()
time.sleep(10)
# Close the browser
driver.quit()
