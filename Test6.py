from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    option1 = browser.find_element_by_css_selector("button.btn")
    option1.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_name("text")
    input1.send_keys(y)
    option3 = browser.find_element_by_css_selector("button.btn")
    option3.click()

finally:
    time.sleep(10)
    browser.quit()
