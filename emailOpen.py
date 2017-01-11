# login to my gmail using Selenium

from selenium import webdriver
import msvcrt , sys

from passHide import hidePassword


			

print ('opening Firefox...')			
browser = webdriver.Firefox()
print ('Done')

print('opening gmail...')
browser.get('https://gmail.com')					
print('Done')					
					
emailElem = browser.find_element_by_id('Email')

my_email = input('Enter your email address: ')
emailElem.send_keys(my_email)	

nextButtonElem = browser.find_element_by_id('next')
nextButtonElem.click()

my_password = hidePassword()
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(my_password)

print('Signing into gmail account...')
passwordElem.submit()



