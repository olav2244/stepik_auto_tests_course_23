from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x1 = x1_element.text

    def calc(x1):
        return str(math.log(abs(12 * math.sin(int(x1)))))

    y = calc(x1)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
