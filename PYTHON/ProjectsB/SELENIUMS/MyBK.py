from selenium import webdriver
from selenium.webdriver.common.by import By
#
username = 'toan.nguyenthai'
password = 'noireNaturai11'
#
driver = webdriver.Chrome('C:\\noirecode\\stuffs\\chrome\\chromedriver.exe')
driver.maximize_window()
#
driver.get('https://sso.hcmut.edu.vn/cas/login?service=http%3A%2F%2Fe-learning.hcmut.edu.vn%2Flogin%2Findex.php%3FauthCAS%3DCAS')
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.NAME, 'submit').click()
#
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window('secondtab')
driver.get('https://mybk.hcmut.edu.vn/stinfo/')
#
driver.execute_script("window.open('about:blank','thirdtab');")
driver.switch_to.window('thirdtab')
driver.get('https://mybk.hcmut.edu.vn/app/')
