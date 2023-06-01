from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    book = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))
    button = browser.find_element(By.XPATH, '//div//button[@id="book"]').click()
    browser.execute_script("window.scrollBy(0, 140);")
    x1 = browser.find_element(By.XPATH, '//div//label//span[@id="input_value"]')
    x = x1.text
    y = calc(x)
    input2=browser.find_element(By.XPATH, '//div//input[@id="answer"]').send_keys(y)
    button1 = browser.find_element(By.ID, 'solve').click()
    browser.execute_script("window.scrollBy(140, 0);")

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

    
