from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui




option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-logging"])
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

#url ="https://www.naver.com"
url = 'https://iris.dongkuk.com/covicore/login.do?isWorksLogout=Y'
driver.get(url)



driver.find_element(By.ID,"idtemp").click()
pyautogui.typewrite("******")
driver.find_element(By.ID,"passwordtemp").click()
pyautogui.typewrite("*******")
driver.find_element(By.CLASS_NAME,"btnLogin").click()