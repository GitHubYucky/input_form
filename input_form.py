from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ytmp3.cc/youtube-to-mp3/")#put here the adress of your page
# elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
input_field = driver.find_element_by_id('input')
# print(elem.get_attribute("class"))
input_text="https://www.youtube.com/watch?v=sToRddIV7kU"
input_field.send_keys(input_text)

submit=driver.find_element_by_id("submit")
submit.click()
download_button=driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
download_button.click()
# driver.close()
