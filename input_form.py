from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ytmp3.cc/youtube-to-mp3/")#put here the adress of your page
# elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
input_field = driver.find_element_by_id('input')
# print(elem.get_attribute("class"))
input_text=""
input_field.send_keys("AAA")
# driver.close()
