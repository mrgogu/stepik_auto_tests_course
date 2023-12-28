from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")

    
    input1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
    input3.send_keys("test@test.com")
    
    button = browser.find_element(By.XPATH, '//button[@type="submit" and text()="Submit"]')
    button.click()

finally:
    
    time.sleep(3)
    browser.quit()
