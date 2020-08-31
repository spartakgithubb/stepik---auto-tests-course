from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("батя")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("батя")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("батя")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)
    option3 = browser.find_element_by_css_selector("button.btn")
    option3.click()

finally:
    time.sleep(10)
    browser.quit()
