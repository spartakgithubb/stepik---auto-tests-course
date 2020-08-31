from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    z = int(num1) + int(num2)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + str(z) + "']").click()
    option3 = browser.find_element_by_css_selector("button.btn")
    option3.click()

finally:
    time.sleep(6)
    browser.quit()
