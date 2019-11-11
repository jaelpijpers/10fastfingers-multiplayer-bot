import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url_main = 'https://10fastfingers.com/multiplayer'
url_game = 'https://10ff.net/login'
username = "JAEL"
driver = webdriver.Firefox()

driver.get(url_game)
time.sleep(3)
#driver.find_element_by_id('CybotCookiebotDialogBodyLevelButtonAccept').click()

driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('username').send_keys(Keys.ENTER)
time.sleep(20)
input_area = driver.find_element_by_class_name('interface')

textlist = driver.find_element_by_class_name('place')
#for word in textlist.find_elements_by_tag_name('span'):
#    driver.find_element_by_tag_name('input').send_keys(word)
#    driver.find_element_by_tag_name('input').send_keys(Keys.SPACE)
while True:
    word = driver.find_element_by_class_name('highlight').text
    driver.find_element_by_tag_name('input').send_keys(word + " ")
    #time.sleep(0.05)



