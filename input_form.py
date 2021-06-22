from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# disable nortifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# Set up driver
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://ytmp3.cc/youtube-to-mp3/")

#input Process
input_text="https://www.youtube.com/watch?v=sToRddIV7kU"
input_field = driver.find_element_by_id('input')
input_field.send_keys(input_text)

# Submit Process
submit=driver.find_element_by_id("submit")
submit.click()

#Download Process
download_button=driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
driver.implicitly_wait(10)
download_button.click()
