from selenium import webdriver
#import time
#import getpass
chrome = webdriver.Chrome()
login = input("Login:\n")
password = input("Password:\n")
#password = getpass.getpass("Password:\n") 
chrome.get('https://www.google.com/')
chrome.find_element_by_id('gb_70').click()
chrome.find_element_by_id('identifierId').send_keys(login)
chrome.find_element_by_id('identifierNext').click()
#time.sleep(2)
chrome.implicitly_wait(2) #it's work for me 
chrome.find_element_by_name('password').send_keys(password)
chrome.find_element_by_id('passwordNext').click()
