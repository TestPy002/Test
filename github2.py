from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pywinauto import Application
import pyautogui as ai
import time

path = 'C:\\Users\\hp\\Downloads\\chromedriver-win6\\chromedriver-win64\\chromedriver.exe'
chrome = webdriver.ChromeOptions()
s = Service(executable_path=path) 
driver = webdriver.Chrome(service=s, options=chrome)
try:
    driver.get('https://github.com/login')
    username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login_field')))
    username.send_keys('TestPy002')
    password = driver.find_element(By.ID, 'password')
    password.send_keys('GoodSurvey1000')
    login_button = driver.find_element(By.XPATH, '//input[@name="commit"]')
    login_button.click()

    try:
        v_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'otp')))
        verification_code = input("Please enter the verification code: ")
        v_input.send_keys(verification_code)
        verify_button = driver.find_element(By.XPATH, '//button[contains(text(), "Verify")]')
        verify_button.click()

    except TimeoutException:
        print("Verification page didn't appear. Proceeding without verification.")

    WebDriverWait(driver, 5).until(EC.url_contains('https://github.com/'))
    print("Done");
    driver.get('https://github.com/TestPy002/Test/upload/main')
    file_add = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#repo-content-pjax-container > div > div.js-upload-manifest-file-container > form:nth-child(2) > file-attachment > p')))
    file_add.click()
    #upload-manifest-files-input #repo-content-pjax-container > div > div.js-upload-manifest-file-container > form:nth-child(2) > file-attachment > p > span
    time.sleep(5)
    ai.typewrite("C:\\Users\\hp\\Downloads\\Test012.c")
    ai.press('enter')
    WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#repo-content-pjax-container > div > div.Box.mb-3.js-manifest-file-list > div > div > form > button > svg > path')))
    time.sleep(10)
    file_ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//p/span[text()="choose your files"]')))
    file_ad.click()
    ai.typewrite("C:\\Users\\hp\\Pictures\\Screenshots\\autotest1.png")
    ai.press('enter')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="autotest2.png"]')))
    commit = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#repo-content-pjax-container > div > form > button')))
    commit.click()
    time.sleep(20)
finally:
    driver.quit()