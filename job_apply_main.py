import os
from time import sleep, time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

Chrome_Dev_path= "E:\Python Udemy\Day 48\Chrome Dev Tools\chromedriver.exe"
driver=Service(Chrome_Dev_path)
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
browser=webdriver.Chrome(service=driver,options=option)

url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
url="https://www.linkedin.com/jobs/search/?currentJobId=3549562130&f_AL=true&f_E=1%2C2&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
browser.get(url)

email="mamun.kfz@gmail.com"
password="mamun464"
MY_PHONE_NUMBER="01767213458"

sign=browser.find_element(By.LINK_TEXT,"Sign in")
#cta-modal__primary-btn btn-md btn-primary inline-block w-full mt-3
sign.click()
user=browser.find_element(By.ID,"username")
user.send_keys(email)
pass1=browser.find_element(By.ID,"password")
pass1.send_keys(password)

sleep(2)
sign=browser.find_element(By.CSS_SELECTOR,".login__form_action_container")
sign.click()
sleep(5)
apply=browser.find_element(By.CLASS_NAME,'jobs-apply-button')
apply.click()

# phn=browser.find_element((By.CLASS_NAME,'artdeco-text-input'))
# phn.send_keys(MY_PHONE_NUMBER)

# press the down arrow button 10 times to scroll down
sleep(2)
click_submit = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()

