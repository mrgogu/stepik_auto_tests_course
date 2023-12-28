import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import time

LINK =  "https://SunInJuly.github.io/execute_script.html"

class MyDriver(webdriver.Chrome):
    def __init__(self,link):
        super().__init__()
        self.get(link)


    def find_x(self):
        return self.find_element(By.CSS_SELECTOR, "#input_value").text
    
    def calc(self):
        return str(math.log(abs(12*math.sin(int(self.find_x())))))
    
    def scroll_page(self):
        self.execute_script("window.scrollBy(0, 100);")
    
    def input_answer(self):
        answer = self.calc()
        answer_input = self.find_element(By.CSS_SELECTOR, "#answer")
        answer_input.send_keys(answer)
        
    def click_checkbox(self):
        return self.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    
    def click_radiobutton(self):
        return self.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    
    def click_submit(self):
        return self.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        

    
if __name__ == "__main__":
    test = MyDriver(LINK)
    try:
        test.scroll_page()        
        test.input_answer()
        test.click_checkbox()
        test.click_radiobutton()
        test.click_submit()
    except exceptions.NoSuchElementException as e:
        time.sleep(10)
        print(e)
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        test.quit()