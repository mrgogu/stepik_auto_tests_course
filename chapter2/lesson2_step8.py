import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions


LINK =  "http://suninjuly.github.io/file_input.html"
TEST_CASE = ["Ivan", "Ivanov", "mail@example.org"]

class MyDriver(webdriver.Chrome):
    def __init__(self,link):
        super().__init__()
        self.get(link)

    def input_requred(self):
        requred_elements = self.find_elements(By.CSS_SELECTOR,'[required]')
        for element, value in zip(requred_elements, TEST_CASE):
            element.send_keys(value)
            
    
    def output_file(self, filename):
        return self.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(filename)
        
    
    def click_submit(self):
        return self.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        

    
if __name__ == "__main__":
    test = MyDriver(LINK)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    try:
        test.input_requred()
        test.output_file(file_path)
        test.click_submit()       
    except exceptions.NoSuchElementException as e:
        time.sleep(10)
        print(e)
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        test.quit()