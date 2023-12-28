import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time

LINK =  "http://suninjuly.github.io/explicit_wait2.html"

class MyDriver(webdriver.Chrome):
    def __init__(self,link):
        super().__init__()
        self.get(link)

    def wait_to_click(self):
        WebDriverWait(self, 5).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
            )
        
        self.find_element(By.ID, "book").click()
    
    def move_new_tab(self):
        print(self.window_handles[-1])
        self.switch_to.window(self.window_handles[-1]) # last tab
    
    def find_x(self):
        return self.find_element(By.CSS_SELECTOR, "#input_value").text
    
    def calc(self):
        return str(math.log(abs(12*math.sin(int(self.find_x())))))
    
    
    def input_answer(self):
        answer = self.calc()
        answer_input = self.find_element(By.CSS_SELECTOR, "#answer")
        answer_input.send_keys(answer)
    
    def click_submit(self):
        return self.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    
    def print_stepik_quiz(self):
        print (self.switch_to.alert.text)
        

    
if __name__ == "__main__":
    test = MyDriver(LINK)
    try:
        test.wait_to_click()
        test.input_answer()
        test.click_submit()
        
        test.print_stepik_quiz()
    except exceptions.NoSuchElementException as e:
        time.sleep(10)
        print(e)
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        test.quit()