from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os

# Web Scraper to upload to contact manager

# URL to be used
url = 'https://survey.intuitionbrandmarketing.com/Member/ContactView/List.action'


# Establishing time 
now = datetime.now()
today_date = now.strftime("%m-%d-%Y")

# login credentials 
user = 'username'
password = 'password'

# Defining paths to files that will be uploaded in contact manager
capital_test = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITAL.csv'

# Chrome established as browser (will check for compatibility)
driver = webdriver.Chrome(ChromeDriverManager().install())

print("\nLet the webscraping begin! \n")


# login 
def login():
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="login"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_id("loginButton").click()
    print('success\n')
    time.sleep(3)
    # contacts tab
    driver.find_element_by_name('LABEL_CONTACTS').click()
    # keys("shift") x 2
    actions = ActionChains(driver)
    print('navigating to contacts...\n')

login()

# CAPITAL TEST block

n = 19
actions.send_keys(Keys. TAB * n)
actions.send_keys(Keys. ENTER)
actions.perform()
print('Capital Test Selected...\n')
time.sleep(3)

# import button 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="divImport"]').click()
# import page -> set up new import
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mainIncludeContainer"]/table/tbody/tr/td/div[1]/button').click()
print('setting up new import...\n')
# choose file
time.sleep(2)
driver.find_element_by_name('localLocation').send_keys(os.path.join(os.getcwd(), capital_test))
print('choosing file...\n')
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/button[2]').click()
driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/button[2]').click()