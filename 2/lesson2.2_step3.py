from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(x1+b1)


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.XPATH, '//div//h2//span[@id="num1"]')
    x1 = int(x.text)
    b = browser.find_element(By.XPATH, '//div//h2//span[@id="num2"]')
    b1 = int(b.text)
    y = calc(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)
    input1 = browser.find_element(By.XPATH, '//div//button[@class="btn btn-default"]').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
