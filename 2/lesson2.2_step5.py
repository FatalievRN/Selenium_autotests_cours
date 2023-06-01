from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.XPATH, '//div//label//span[@id="input_value"]')
    x = x1.text
    y = calc(x)
    input1=browser.find_element(By.XPATH, '//div//input[@id="answer"]')
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 110);")
    imrobot = browser.find_element(By.XPATH, '//div//input[@class="form-check-input"]').click()
    check = browser.find_element(By.XPATH, '//div//input[@id="robotsRule"]').click()
    button = browser.find_element(By.XPATH, '//div//button[@class="btn btn-primary"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
