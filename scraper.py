from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os

# Web Scraper to upload to contact manager

now = datetime.now()
today_date = now.strftime("%m-%d-%Y")

print('')
print("Let the webscraping begin! \n")

url = 'https://survey.intuitionbrandmarketing.com/Member/ContactView/List.action'
driver = webdriver.Chrome(ChromeDriverManager().install())
# userID = driver.find_element_by_xpath('//*[@id="login"]')
# auto log into site

# login 
driver.get(url)
driver.find_element_by_xpath('//*[@id="login"]').send_keys("email")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("password")
driver.find_element_by_id("loginButton").click()
print('success\n')
time.sleep(3)
# contacts tab
driver.find_element_by_name('LABEL_CONTACTS').click()
# keys("shift") x 2
actions = ActionChains(driver)
print('navigating to contacts...\n')

# capital
# selects CAPITAL TEST
n = 19
actions.send_keys(Keys. TAB * n)
actions.send_keys(Keys. ENTER)
actions.perform()
print('Capital Started...\n')
time.sleep(3)

# import
time.sleep(2)
driver.find_element_by_xpath('//*[@id="divImport"]').click()
# import page set up new import
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mainIncludeContainer"]/table/tbody/tr/td/div[1]/button').click()
print('set up new import')
# choose file
time.sleep(2)
driver.find_element_by_name('localLocation').send_keys(os.path.join(os.getcwd(), '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITAL.csv'))
print('choosing file...\n')
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/button[2]').click()
driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/button[2]').click()