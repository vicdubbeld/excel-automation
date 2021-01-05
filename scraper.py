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
user = 'victordubbeld@intuitionbrandmarketing.com'
password = 'intuition'

# Defining paths to files that will be uploaded in contact manager
path = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date
capital_test = path +'CAPITAL.csv'

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
    print('navigating to contacts...\n')
login()

# CAPITAL TEST block

# tabbing to CAPITAL TEST

# keys("shift") x 2
actions = ActionChains(driver)

n = 19
actions.send_keys(Keys. TAB * n)
actions.send_keys(Keys. ENTER)
actions.perform()
print('Capital Test Selected...\n')
time.sleep(3)

# def import_task(n, file,  ):
#     # select contact
#     actions.send_keys(Keys. TAB * n)
#     # 

# Selects import button 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="divImport"]').click()

# import page -> set up new import
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mainIncludeContainer"]/table/tbody/tr/td/div[1]/button').click()
print('setting up new import...\n')
# chooses file
time.sleep(2)
driver.find_element_by_name('localLocation').send_keys(os.path.join(os.getcwd(), capital_test))
print('choosing file...\n')
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/button[2]').click()
driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/button[2]').click()
# return to contact page

# Next step...navigate to Surveys tab
# Further down the line...

# Only launch surveys for clients who had files imported into contact manager...
# In contact manager page, each one has a set # of times to press TAB in order to navigate to it. 
# Other than that, everything should be the same process up until launching the surveys

# 1 Login (1)
# 2 Contacts page (1)

# 3 select contact (filename, n(tabs), )
    # 4 import file 
    # 5 verify
    # 6 go back to Contact page (step 2) x n

# 7 Surveys page
# 8 Select survey
# 9 Launch n times