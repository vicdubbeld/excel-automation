from selenium import webdriver

# Web Scraper to upload to contact manager

print('')
print("Let the webscraping begin! \n")

url = 'https://survey.intuitionbrandmarketing.com/Member/ContactView/List.action'
browser = webdriver.Chrome()

browser.find_element_by_xpath('//*[@id=treeViewNode_1_-41512190_1_41512190"]').click()