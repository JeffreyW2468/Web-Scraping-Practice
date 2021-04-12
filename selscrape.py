from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/jeff/Desktop/scrapin_stuffs/chromedriver')
driver.get('https://meta.discourse.org/')
print(driver.title)
main_data = driver.find_element_by_xpath("/html/body/section/div/div[5]/div[5]/div[2]/div/div/div/table/tbody")
#print(main_data.get_attribute('innerHTML'))

for each in main_data.find_elements_by_xpath(".//tr"):
    print(each.find_elements_by_xpath(".//*[@class='number']")[1].get_attribute('innerHTML'))
    
driver.close()