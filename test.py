import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.shazam.com/")
textarea = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/input').send_keys('user')
pas = driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/input').send_keys('1')
time.sleep(2)
enter = driver.find_element_by_xpath('/html/body/div[1]/div/div[8]').click()
time.sleep(2)
key = driver.find_element_by_xpath('/html/body/div[1]/div/div[7]/input').send_keys('')
time.sleep(2)
enter = driver.find_element_by_xpath('/html/body/div[1]/div/div[8]').click()
time.sleep(5)
ch = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[12]/div').click()
time.sleep(2)
pl = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[4]/button[1]').click()
time.sleep(2)
driver.close()
quit()