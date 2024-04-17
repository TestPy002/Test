from selenium import webdriver #webdriver conations all functions to operate webpage
from selenium.webdriver.chrome.service import Service #service function that runs the exe file of browser

# Path to the ChromeDriver executable
path = 'C:\\Users\\hp\\Downloads\\chromedriver-win6\\chromedriver-win64\\chromedriver.exe'  # Windows example

c = webdriver.ChromeOptions() # c is object/variable for specfically chrome, is initailised with chromeoptions() function
# chrome_options.add_argument('--headless')  # Uncomment to run in headless mode (without opening a visible browser window)
#as above chromeoption function takes some optional arguements depending as u want
s = Service(executable_path=path) #s is object/variable that holds path of chromedriver using service function
d = webdriver.Chrome(service=s, options=c) #d is driver object that takes s and c to run chrome
#d in others is now chrome
try:
    # Navigate to a webpage
    d.get('https://www.example.com/login') #get() runs website on d(chrome)
    # Extract the title of the page
    title = d.title
    print("Page Title:", title)

finally:
    # Close the browser window
    d.quit()
