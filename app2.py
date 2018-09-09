from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('/Users/goosini/chromedriver')
for i in range(0,999):
    driver.find_element_by_css_selector("#main > footer > div._3pkkz.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text").send_keys("take ear phones")
    driver.find_element_by_css_selector("#main > footer > div._3pkkz.copyable-area > div:nth-child(3) > button > span").click()
    print(i)
    #Sending whatsapp messages to a contact in bulk.