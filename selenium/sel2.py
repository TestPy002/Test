from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Path to the ChromeDriver executable
path = 'C:\\Users\\hp\\Downloads\\chromedriver-win6\\chromedriver-win64\\chromedriver.exe'  # Windows example

# Optional: Specify options for Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Uncomment to run in headless mode (without opening a visible browser window)
s = Service(executable_path=path) 
# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(service=s, options=chrome_options)

try:
    # Navigate to the GitHub login page
    driver.get('https://github.com/login')

    # Wait for the username input field to be visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'login_field'))
    )

    # Enter the username
    username_input.send_keys('TestPy002')

    # Locate the password input field
    password_input = driver.find_element(By.ID, 'password')

    # Enter the password
    password_input.send_keys('GoodSurvey1000')

    # Click the login button
    login_button = driver.find_element(By.XPATH, '//input[@name="commit"]')
    login_button.click()

    try:
        # Wait for the verification code input field to be visible
        verification_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'otp'))
        )

        # Prompt the user to enter the verification code
        verification_code = input("Please enter the verification code: ")

        # Enter the verification code
        verification_input.send_keys(verification_code)

        # Click the "Verify" button
        verify_button = driver.find_element(By.XPATH, '//button[contains(text(), "Verify")]')
        verify_button.click()

    except TimeoutException:
        # If the verification page doesn't appear within the timeout, proceed without verification
        print("Verification page didn't appear. Proceeding without verification.")

    # Wait for the login process to complete
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://github.com/')
    )
    print("Done");
    # Extract and print the username of the logged-in user
    username_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="dashboard"]/div/feed-container/div[3]/article[1]/div/div[1]/section/h4'))
    )
    username = username_element.get_attribute('innerText')
    print("Logged in as:", username)

finally:
    # Close the browser window
    driver.quit()
