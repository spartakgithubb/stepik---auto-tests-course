from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    people_radio = browser.find_element_by_tag_name("img")
    x_element = people_radio.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    option3 = browser.find_element_by_css_selector("button.btn")
    option3.click()

finally:
    time.sleep(10)
    browser.quit()
