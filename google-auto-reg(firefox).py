from selenium import webdriver
import time, getpass

login = input('username: ')
password = getpass.getpass(prompt='password (hidden): ')

print('Wait...')

fox = webdriver.Firefox()
fox.get('https://www.google.com')
fox.find_element_by_id('gb_70').click()
fox.find_element_by_id('identifierId').send_keys(login)
fox.find_element_by_id('identifierNext').click()
time.sleep(1)
# unfortunately, "fox.implicitly_wait(2)" did not work for me
fox.find_element_by_name('password').send_keys(password)
fox.find_element_by_id('passwordNext').click()
