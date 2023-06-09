from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure1=browser.find_element(By.ID, 'treasure')
    
    x_element = treasure1.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input1=browser.find_element(By.XPATH, '//div//input[@id="answer"]')
    input1.send_keys(y)
    input2=browser.find_element(By.XPATH, '//div//input[@id="robotCheckbox"]').click()
    input3=browser.find_element(By.XPATH, '//div//input[@id="robotsRule"]').click()
    input4=browser.find_element(By.XPATH, '//div//button[@class="btn btn-default"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
