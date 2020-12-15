from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Web Scraper to upload to contact manager

print('')
print("Let the webscraping begin! \n")

url = 'https://survey.intuitionbrandmarketing.com/Member/ContactView/List.action'
driver = webdriver.Chrome(ChromeDriverManager().install())
# userID = driver.find_element_by_xpath('//*[@id="login"]')
# auto log into site

driver.get(url)
driver.find_element_by_xpath('//*[@id="login"]').send_keys("{email}")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("{password}")
driver.find_element_by_id("loginButton").click()
print('success')

driver.find_element_by_name('LABEL_CONTACTS').click()
# keys("shift") x 2
actions = ActionChains(driver)
n = 18
actions.send_keys(Keys. TAB * n)
actions.send_keys(Keys. ENTER)
actions.perform()

# driver.find_element_by_xpath('/html/body/form/div[3]/ul/li[5]/a').click()


# site_login()
# browser.find_element_by_xpath('//*[@id="treeViewNode_1_-41512190_1_41512190"]').click()
