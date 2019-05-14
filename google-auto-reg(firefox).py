from selenium import webdriver
import time
import getpass
login = input("Login: ")
password = getpass.getpass(prompt='password (hidden): ')
# a path should be specified on your own (don't forget that for Windows we use double-backslash \\ ) 
# however we don't need the path if there is driver in the same directory with .py
# so, '''fox = webdriver.Firefox(executable_path="C:\\geckodriver.exe")''' is not necessary.
fox = webdriver.Firefox()
fox.get('https://www.google.com')
fox.find_element_by_id('gb_70').click()
fox.find_element_by_id('identifierId').send_keys(login)
fox.find_element_by_id('identifierNext').click()
time.sleep(1)
# unfortunately, "fox.implicitly_wait(2)" did not work for me
fox.find_element_by_name('password').send_keys(password)
fox.find_element_by_id('passwordNext').click()
