from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("C:\Users\joshi\Downloads\chromedriver_win32")
# driver.get ("http://127.0.0.1:8000/signin")

# driver.find_element_by_name("username").send_keys("yashas")
# driver.find_element_by_name("pass1").send_keys("1234@abcd")
# submit = driver.find_element_by_name("btn-login")
# submit.send_keys(Keys.RETURN)

USERNAME= 'yashas'
PASSWORD= '1234@abcd'
EMAIL= 'yashas@gmail.com'
MESSAGE= 'Hello'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://127.0.0.1:8000/signin')

user_input = driver.find_element_by_id('username')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('pass1')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('btn-login')
login_button.click()

#Scroll Functionality

time.sleep(4)

element = driver.find_element_by_tag_name('body')

while True:
    element.send_keys(Keys.END)
    time.sleep(4)
    break


driver.get('http://127.0.0.1:8000/aboutus')

time.sleep(4)
element = driver.find_element_by_tag_name('body')

while True:
    element.send_keys(Keys.END)
    time.sleep(4)
    break

driver.get('http://127.0.0.1:8000/contactus')
user_input = driver.find_element_by_id('contact-name')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('contact-email')
password_input.send_keys(EMAIL)

password_input = driver.find_element_by_id('contact-message')
password_input.send_keys(MESSAGE)

login_button = driver.find_element_by_id('btn-contact')
login_button.click()

time.sleep(5)
driver.close()





