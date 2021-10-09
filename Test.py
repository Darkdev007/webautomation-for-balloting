from os import terminal_size
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://studentportal.unilag.edu.ng/(S(sea0egc1uuv0cmrsbotpekjc))/default.aspx")
refresh_time_in_seconds = 10
while True:
    try:
        driver.find_element_by_id('UsernameTextBox')
        break
    except (NoSuchElementException):
        time.sleep(refresh_time_in_seconds)
        driver.refresh()

MatricNo = driver.find_element_by_id('UsernameTextBox')
MatricNo.send_keys('180401009')
Password = driver.find_element_by_id('PasswordTextBox')
Password.send_keys('jambregistration')
MatricNo.send_keys( Keys.ENTER)


elem = driver.find_element_by_link_text('Course Registration')
elem.click()


"""  
refresh_time_in_seconds = 15
driver.get("https://studentportal.unilag.edu.ng/(S(sea0egc1uuv0cmrsbotpekjc))/default.aspx")
url = driver.current_url
while(True):
    if url == driver.current_url:
        driver.refresh()
    url = driver.current_url
    time.sleep(refresh_time_in_seconds)
"""

        
"""
driver.get("https://studentportal.unilag.edu.ng/(S(sea0egc1uuv0cmrsbotpekjc))/default.aspx")

while True:
    if any(["Puffy" in h1.text.replace('\uFEFF', "") for h1 in driver.find_elements_by_id("name-link")]):
        break
    else:
        driver.refresh
"""