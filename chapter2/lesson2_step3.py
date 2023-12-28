import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import time

LINK =  "http://suninjuly.github.io/selects1.html"

class MyDriver(webdriver.Chrome):
    def __init__(self,link):
        super().__init__()
        self.get(link)


    def find_num1(self):
        return self.find_element(By.CSS_SELECTOR, "#num1").text
    
    def find_num2(self):
        return self.find_element(By.CSS_SELECTOR, "#num2").text
    
    def calc(self):
        return int(self.find_num1()) + int(self.find_num2())
    
    def select_answer(self):
        answer = str(self.calc())
        answer_input = Select(self.find_element(By.TAG_NAME, "select"))
        answer_input.select_by_value(answer)
        
    
    def click_submit(self):
        return self.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        

    
if __name__ == "__main__":
    test = MyDriver(LINK)
    try:        
        test.select_answer()
        test.click_submit()
    except exceptions.NoSuchElementException as e:
        time.sleep(10)
        print(e)
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        test.quit()