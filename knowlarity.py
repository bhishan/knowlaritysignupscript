from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("http://knowlarity.com")
sign_up_submit = browser.find_elements_by_xpath("//*[contains(text(),'Try Free-for-Life')]")
sign_up_submit[4].click()
name = browser.find_element_by_name("contact-name")
name.send_keys("Bhishan Bhandari")
email = browser.find_element_by_name("contact-email")
email.send_keys("bbhishan@gmail.com")
phone = browser.find_element_by_name("contact-phone")
phone.send_keys("9849060230")
phone.send_keys(Keys.RETURN)
