from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(4)
    input1 = browser.find_element(By.XPATH,'//div//button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(4)
    x1 = browser.find_element(By.XPATH, '//div//label//span[@id="input_value"]')
    x = x1.text
    y = calc(x)
    input2=browser.find_element(By.XPATH, '//div//input[@id="answer"]').send_keys(y)
    button = browser.find_element(By.XPATH, '//div//button[@class="btn btn-primary"]').click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()

    
