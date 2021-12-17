from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("C:\Users\joshi\Downloads\chromedriver_win32")
# driver.get ("http://127.0.0.1:8000/signin")

# driver.find_element_by_name("username").send_keys("yashas")
# driver.find_element_by_name("pass1").send_keys("1234@abcd")
# submit = driver.find_element_by_name("btn-login")
# submit.send_keys(Keys.RETURN)

USERNAME= 'yashas'
PASSWORD= '1234@abcd'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://127.0.0.1:8000/signin')

user_input = driver.find_element_by_id('username')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('pass1')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('btn-login')
login_button.click()


