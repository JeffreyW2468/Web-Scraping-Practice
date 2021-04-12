from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/jeff/Desktop/scrapin_stuffs/chromedriver')
driver.get('https://meta.discourse.org/')
print(driver.title)
search_bar = driver.find_element_by_id("search-term")
search_bar.clear()
search_bar.send_keys("error")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()