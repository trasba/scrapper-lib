#!/usr/bin/env python
# coding: utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime
import time

strUser = 'XXXXX'
strPass = 'XXXXX'
strPath = 'XXXXX'
intCount = 2

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)
driver.get("https://accounts.ww-ag.de/login.wv")

elem1 = wait.until(EC.element_to_be_clickable((By.ID, 'WW_login-username')))
elem1.click()
elem1.clear()
elem1.send_keys(strUser)

elem2 = driver.find_element_by_id("WW_login-password")
elem2.click()
elem2.clear()
elem2.send_keys(strPass)
elem2.send_keys(Keys.RETURN)

elem3 = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Vertragsübersicht')))
elem3.click()
wait.until(EC.frame_to_be_available_and_switch_to_it("B2CPortalIfr"))

elem4 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'leftJustifyStyle')))
elem4 = driver.find_elements_by_class_name("leftJustifyStyle")
str1 = []
for x in range(0, intCount):
        str1.append((elem4[3*x+2].get_attribute("innerHTML"))[:-4])

strDate = datetime.datetime.today().strftime('%Y%m%d')

f = open(strPath + strDate + '.csv', 'a')
for x in range(0, intCount):
        f.write('"' + str1[x] + '","Wuestenrot' + str(x) + '_Saldo"\n')
f.close()

driver.quit()
