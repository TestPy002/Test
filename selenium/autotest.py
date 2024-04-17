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
    driver.get('https://github.com/Ashank7/DSA-IN-C')
    Cfile=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#folder-row-5 > td.react-directory-row-name-cell-large-screen > div > div > h3 > div > a')))
    Cfile.click()
    dwld=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#repos-sticky-header > div.Box-sc-g0xbh4-0.ePiodO > div.Box-sc-g0xbh4-0.jfjHXm > div.Box-sc-g0xbh4-0.iBylDf > div.Box-sc-g0xbh4-0.kSGBPx.react-blob-header-edit-and-raw-actions > div:nth-child(1) > span > button > svg > path:nth-child(2)')))
    dwld.click()
    time.sleep(5)
    vscode = Application().start("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    time.sleep(5)
    ai.hotkey('ctrl','o')
    time.sleep(1)
    ai.typewrite("C:\\Users\\hp\\Downloads\\Exp2.c")
    ai.press('enter')
    ai.hotkey('winleft','up')
    time.sleep(1)
    ai.hotkey('ctrl','a')
    ai.hotkey('ctrl','c')
    ai.hotkey('ctrl','n')
    ai.hotkey('ctrl','v')
    ai.hotkey('ctrl','s')
    time.sleep(2)
    ai.typewrite("Test012.c")
    ai.press('enter')
    time.sleep(2)
    ai.hotkey('ctrl','alt','c')
    time.sleep(30)
    ai.hotkey('winleft','shift','s')
    time.sleep(20)
    ai.click(x=1200, y=600)
    ai.hotkey('winleft','up')
    ai.hotkey('ctrl','s')
    time.sleep(5)
    ai.typewrite("autotest2")
    ai.press('enter')
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
    #menu=driver.find_element(By.XPATH,"//button[@aria-label='Open user account menu']")
    #menu.click() 
    #dbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//dialog-helper/dialog[@aria-modal='true']")))
    #test= driver.find_element(By.XPATH, '//a[contains(@href, "/TestPy002/Test")]')
    #test.click()
    #add=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#\\:R2hil5\\: > svg")))
    #add.click()
    #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(@href,"/TestPy002/Test/upload/main")]'))).click()
    driver.get('https://github.com/TestPy002/Test/upload/main')
    file_add = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#repo-content-pjax-container > div > div.js-upload-manifest-file-container > form:nth-child(2) > file-attachment > p')))
    file_add.click()
    time.sleep(5)
    ai.typewrite("C:\\Users\\hp\\Downloads\\Test012.c")
    ai.press('enter')
    WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#repo-content-pjax-container > div > div.Box.mb-3.js-manifest-file-list > div > div > form > button > svg > path')))
    time.sleep(10)
    file_add = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#repo-content-pjax-container > div > div.js-upload-manifest-file-container > form:nth-child(2) > file-attachment > p')))
    file_add.click()
    ai.typewrite("autotest2.png")
    ai.press('enter')
    commit = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#repo-content-pjax-container > div > form > button')))
    commit.click()
    time.sleep(20)
finally:
    # Close the browser window
    #WebDriverWait(driver,20)
    driver.quit()
    
